import requests
import json

url = "https://pingrural.onrender.com/"  # <- tem que ser essa URL

payload = {
    "entry": [
        {
            "id": "fake_id",
            "changes": [
                {
                    "value": {
                        "messages": [
                            {
                                "from": "556799999999",
                                "text": {
                                    "body": "Teste local do Ping Rural"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    ]
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, data=json.dumps(payload))
print("Status:", response.status_code)
print("Resposta:", response.text)
