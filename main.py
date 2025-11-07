# main.py
import os
import json
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from agent import Agent

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
HOST = os.getenv("HOST", "http://localhost:5000")
PORT = int(os.getenv("PORT", 5000))

if not TELEGRAM_TOKEN:
    raise ValueError("Defina TELEGRAM_BOT_TOKEN no .env")

app = Flask(__name__)
agent = Agent()

@app.route("/webhook", methods=["POST"])
def webhook():
    update = request.json
    # Extrai mensagem de texto básica do Telegram
    try:
        chat_id = update["message"]["chat"]["id"]
        text = update["message"].get("text", "")
    except Exception:
        # ignora updates que não são mensagem de texto
        return jsonify({"status": "ignored"}), 200

    # Processa via agente
    response_text = agent.handle_message(text, metadata={"chat_id": chat_id})

    # Responde via Telegram API
    send_message(chat_id, response_text)
    return jsonify({"status": "ok"}), 200

def send_message(chat_id, text):
    import requests
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    requests.post(url, json=payload)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)
