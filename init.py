import requests as requests
from dotenv import load_dotenv
import os

load_dotenv()
def setWebhook():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    payload = {"url": "https://flask-test-becva.run.goorm.site/"}
    requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook", params=payload)

setWebhook()