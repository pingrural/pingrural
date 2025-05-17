from flask import Flask, request
import json

app = Flask(__name__)

VERIFY_TOKEN = "pingrural123"

@app.route('/', methods=['GET', 'POST'])
def webhook():
    print("📡 Requisição recebida:", request.method)

    if request.method == 'GET':
        print("🔍 Verificando webhook...")
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("✅ Webhook verificado com sucesso!")
            return challenge, 200
        else:
            print("❌ Token inválido!")
            return "Token inválido", 403

    elif request.method == 'POST':
        print("📨 Entrou no bloco POST")
        try:
            data = request.get_json()
            print("📦 Conteúdo recebido:")
            print(json.dumps(data, indent=2))
        except Exception as e:
            print("❌ Erro ao decodificar JSON:", e)

        return "Mensagem recebida", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
