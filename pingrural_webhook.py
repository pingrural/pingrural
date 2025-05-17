from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "pingrural123"

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            print("✅ Webhook verificado com sucesso!")
            return challenge, 200
        else:
            return "Token inválido", 403

    elif request.method == 'POST':
        data = request.get_json()
        print("📨 Mensagem recebida:", data)
        return "Mensagem recebida", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
