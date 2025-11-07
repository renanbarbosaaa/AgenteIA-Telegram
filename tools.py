# tools.py
import time
import uuid

def create_ticket_tool(data: dict):
    """Simula criação de ticket em um sistema."""
    ticket_id = str(uuid.uuid4())[:8]
    # aqui você poderia inserir em banco de dados, enviar para n8n webhook, etc.
    time.sleep(0.3)
    return {"id": ticket_id, "title": data.get("title"), "status": "created"}

def lookup_product_tool(query: str):
    """Simula busca de produto (mock)."""
    sample_db = [
        {"sku": "001", "name": "Pizza Margherita", "price": 23.5},
        {"sku": "002", "name": "Coca-Cola 350ml", "price": 6.0},
        {"sku": "003", "name": "Burger Simples", "price": 18.0},
    ]
    if not query:
        return sample_db
    results = [p for p in sample_db if query.lower() in p["name"].lower()]
    return results or {"message": "Nenhum produto encontrado"}
