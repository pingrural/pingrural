from flask import Flask, request
import json
import os
import logging

# Configuração do logging para aparecer nos logs da Render
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

VERIFY_TOKEN = "pingrural123"

@app.route('/', methods=['GET', 'POST'])
def webhook():
    logger.info("📡 Requisição recebida: %s", request.method)

    if request.method == 'GET':
        logger.info("🔍 Verificando webhook...")
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == VERIFY_TOKEN:
            logger.info("✅ Webhook verificado com sucesso!")
            return challenge, 200
        else:
            logger.warning("❌ Token inválido!")
            return "Token inválido", 403

    elif request.method == 'POST':
        logger.info("📨 Entrou no POST do Ping Rural")
        try:
            logger.info("🧪 Headers recebidos: %s", dict(request.headers))

            raw_body = request.data.decode("utf-8")
            logger.info("📨 Corpo bruto da requisição: %s", raw_body)

            data = request.get_json(force=True, silent=False)
            if data is None:
                logger.warning("⚠️ Nenhum JSON detectado!")
            else:
                logger.info("📦 JSON decodificado com sucesso:\n%s", json.dumps(data, indent=2))
        except Exception as e:
            logger.error("❌ Erro ao processar POST: %s", e)

        return "Mensagem recebida", 200

    return "Método não suportado", 405

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
