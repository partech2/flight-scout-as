import requests

BOT_TOKEN = "PUT_YOUR_BOT_TOKEN_HERE"
CHAT_ID = "PUT_YOUR_CHAT_ID_HERE"

def send_message(text):
    url = f"https://api.telegram.org/bot8849402484:AAFvU1fxywaWk9r9O5slmq8iO7MyDrCDvBE/sendMessage"

    payload = {
        "chat_id": 5029616223,
        "text": text
    }

    response = requests.post(url, json=payload)
    print(response.json())

send_message("✈️ Travel Scout AI is alive!")
