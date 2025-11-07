# Telegram AI Agent

Agente conversacional em Python que integra Telegram + OpenAI para processar mensagens, classificar intenções e executar *tools* (ações) — ideal como projeto demonstrativo de IA aplicada.

**Funcionalidades**
- Respostas baseadas em modelos OpenAI (chat)
- Pipeline de agente que decide quando chamar *tools* (ex.: criar ticket, buscar dados)
- Exemplo de ferramentas (criar ticket mock, buscar produto)
- Fácil de estender e integrar com n8n, APIs externas ou banco de dados

## Tecnologias
- Python 3.10+
- Flask (webhook para Telegram)
- requests
- python-dotenv
- openai

## Como rodar (local)
1. Clone o repositório:
```bash
git clone https://github.com/SEU-USERNAME/telegram-ai-agent.git
cd telegram-ai-agent
```

2. Crie e ative um virtualenv:
```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate    # Windows
```

3. Instale dependências:
```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` a partir de `.env.example` e preencha:
```
TELEGRAM_BOT_TOKEN=seu_token_telegram
OPENAI_API_KEY=sua_chave_openai
HOST=https://seu-dominio-ou-ngrok
PORT=5000
```

5. Exponha local para testes (ex.: ngrok) e configure webhook do Telegram:
```bash
# rodar app
python main.py
# em outra janela (ex.: com ngrok)
ngrok http 5000
# defina TELEGRAM webhook apontando para https://<ngrok-id>.ngrok.io/webhook
```

6. Teste no Telegram conversando com o bot.

## Arquitetura
- `main.py`: servidor Flask que recebe webhook do Telegram
- `agent.py`: pipeline do agente — gera prompt, chama OpenAI e decide chamar tools
- `tools.py`: ferramentas que o agente pode executar (ex.: criar ticket mock)
- `.env`: configurações sensíveis

## Como demonstrar no GitHub
- Adicione screenshots de uma conversa
- Mostre um vídeo curto (GIF/MP4) do agente respondendo e executando um *tool* (ex.: criar ticket)
- Documente casos de uso (suporte, automação, classificação)

## Licença
MIT
