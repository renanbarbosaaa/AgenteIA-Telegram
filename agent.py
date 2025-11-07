# agent.py
import os
import json
import openai
from tools import create_ticket_tool, lookup_product_tool

openai.api_key = os.getenv("OPENAI_API_KEY")

class Agent:
    """
    Pipeline simples:
    - Recebe mensagem do usuário
    - Envia para o modelo com instruções (system prompt)
    - Verifica se a resposta requer execução de ferramenta (usando tags)
    - Executa tool se necessário e responde com resultado
    """

    SYSTEM_PROMPT = """
Você é um assistente virtual que decide quando chamar ferramentas.
Se o usuário pede para criar um ticket, retorne: CALL_TOOL:CREATE_TICKET {json_payload}
Se o usuário pede para buscar produto, retorne: CALL_TOOL:LOOKUP_PRODUCT {json_payload}
Caso contrário, responda diretamente.
"""

    def __init__(self, model="gpt-3.5-turbo"):
        self.model = model

    def handle_message(self, message, metadata=None):
        # Gera resposta do modelo
        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {"role": "user", "content": message}
            ],
            max_tokens=300
        )
        text = completion["choices"][0]["message"]["content"].strip()

        # Detecta comando CALL_TOOL:
        if text.startswith("CALL_TOOL:"):
            try:
                header, payload = text.split(None, 1)  # separa "CALL_TOOL:NAME" e JSON
            except ValueError:
                return "Desculpe, não entendi a solicitação da ferramenta."

            # header ex: CALL_TOOL:CREATE_TICKET
            tool_name = header.split(":")[1]
            if tool_name == "CREATE_TICKET" or tool_name == "CALL_TOOL:CREATE_TICKET":
                # espera payload json
                import json
                try:
                    data = json.loads(payload)
                except Exception:
                    return "Payload inválido para criação de ticket."
                result = create_ticket_tool(data)
                return f"Ticket criado: {result}"
            elif tool_name == "LOOKUP_PRODUCT" or tool_name == "CALL_TOOL:LOOKUP_PRODUCT":
                import json
                try:
                    data = json.loads(payload)
                    query = data.get("query") if isinstance(data, dict) else None
                except Exception:
                    query = None
                result = lookup_product_tool(query)
                return f"Resultado de busca: {result}"
            else:
                return "Tool não reconhecida."
        else:
            return text
