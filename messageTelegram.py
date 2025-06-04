import requests

# Sostituisci con il tuo token del bot e il tuo chat_id
TOKEN = "7317796664:AAH47DgZH3env8-pN18kUcuE7ukJiVSr3sI"
CHAT_ID = '1118359163'
MESSAGE = 'Ciao!!!'

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

def send_message_cele(message):
    send_message(TOKEN, CHAT_ID, message)

def send_message(token, chat_id, message):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print('Messaggio inviato con successo!')
    else:
        print('Errore nell\'invio del messaggio:', response.text)

if __name__ == '__main__':
    send_message(TOKEN, CHAT_ID, MESSAGE)