import os
import asyncio
from telegram import Bot
import requests
from firestore import db

BASE_URL = os.getenv('BASE_URL')
BOT_TOKEN = os.getenv('BOT_TOKEN')

def lambda_handler(event, context):
    asyncio.run(send_quote(author_name='Friedrich_Nietzsche',
                bot_token=BOT_TOKEN))
    return


async def send_quote(author_name: str, bot_token: str):
    bot = Bot(token=bot_token)
    subscribers = get_subscribers(author_name=author_name)
    quote = get_random_quote(author_name=author_name)

    for subscriber in subscribers:
        try:
            await bot.send_message(chat_id=subscriber["chatId"], text=quote)
            print("Quote sent to subscribers")
        except Exception as err:
            error_message = f"Error sending quote to {subscriber['name']}"
            print(error_message, err)


def get_random_quote(author_name: str):
    response = requests.get(
        f'{BASE_URL}/authors/{author_name}/randomquote')
    quote_content = response.json()['content']
    full_quote = f"{quote_content}"
    return full_quote


def get_subscribers(author_name: str) -> list:
    subscribers_collection = db.collection(
        "authors").document(author_name).collection("subscribers")
    subscribers = subscribers_collection.get()
    return subscribers
