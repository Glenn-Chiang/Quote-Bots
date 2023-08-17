from telegram import Update
from telegram.ext import Application, CallbackContext, CommandHandler
import requests
import os
from dotenv import load_dotenv
load_dotenv()

class User():
    def __init__(self, name, chat_id) -> None:
        self.name = name
        self.chat_id = chat_id


def register_user(update: Update, context: CallbackContext):
    username = update.effective_user.username
    chat_id = update.effective_chat.id

    user = User(name=username, chat_id=chat_id)
    base_url = os.environ.get('BASE_URL')
    requests.post("/authors/Friedrich_Nietzsche/subscribers", json=user)

    update.message.reply_text(text="Registration successful")

def main():
    app = Application.builder().token(os.getenv('BOT_TOKEN')).build()
    app.add_handler(CommandHandler('start', register_user))