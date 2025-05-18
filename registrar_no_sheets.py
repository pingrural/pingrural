import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# Autenticação com o Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("pingrural-credentials.json", scope)
client = gspread.authorize(creds)

# Acessar planilha e aba
spreadsheet = client.open_by_key("1MBR8ye3_Cqc2eSkG-jBA4baLIDvLFQB0hELBXHr09RI")
sheet = spreadsheet.worksheet("mensagens_recebidas")

def registrar_mensagem(numero, mensagem):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    sheet.append_row([agora, numero, mensagem])
    print(f"✅ Registrado: {numero} - {mensagem}")
