import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
import os
import base64

# Reconstrói o JSON de credenciais a partir de variável de ambiente
base64_creds = os.environ.get("GOOGLE_CREDENTIALS_BASE64")
if base64_creds:
    with open("pingrural-credentials.json", "wb") as f:
        f.write(base64.b64decode(base64_creds))

# Autenticação com o Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("pingrural-credentials.json", scope)
client = gspread.authorize(creds)

# Acessar planilha e aba
spreadsheet = client.open_by_key("1MBR8ye3_Cqc2eSkG-jBA4baLIDvLFQB0hELBXHr09RI")
sheet = spreadsheet.worksheet("mensagens_recebidas")

def registrar_mensagem(numero, mensagem):
    print("📥 Função registrar_mensagem chamada.")
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    sheet.append_row([agora, numero, mensagem])
    print(f"✅ Registrado: {numero} - {mensagem}")
