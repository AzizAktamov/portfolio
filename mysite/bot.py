import requests
from config.settings import BOT_TOKEN,CHAT_ID

def send_message(name,email,phone_numer,description):
    text = f"NAME : {name}\nEMAIL : {email}\nPHONE : {phone_numer}\nTEXT : {description}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/SendMessage?chat_id={CHAT_ID}&text={text}"
    requests.get(url)