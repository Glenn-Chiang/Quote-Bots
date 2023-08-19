import os
import asyncio
from telegram import Bot
import requests
from dotenv import load_dotenv
load_dotenv()


def lambda_handler(event, context):
    asyncio.run(main())
    return


async def main():
    author_name = 'Friedrich_Nietzsche'
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    subscribers = get_subscribers(author_name=author_name)
    quote = get_random_quote(author_name=author_name)

    for subscriber in subscribers:
        try:
            await bot.send_message(chat_id=subscriber["chat_id"], text=quote)
            print("Quote sent to subscribers")
        except Exception as err:
            error_message = f"Error sending quote to {subscriber['username']}"
            print(error_message, err)


def get_random_quote(author_name: str):
    response = requests.get(
        f"{os.getenv('BASE_URL')}/authors/{author_name}/randomquote")
    quote_content = response.json()['content']
    full_quote = f"{quote_content}"
    return full_quote


def get_subscribers(author_name: str) -> list:
    # subscribers_collection = db.collection(
    #     "authors").document(author_name).collection("subscribers")
    # subscriberDocs = subscribers_collection.stream()
    # subscribers = [doc.to_dict() for doc in subscriberDocs]
    subscribers = [{"username": "Glenn_Chiang", "chat_id": "5291406801"}]
    return subscribers


if __name__ == '__main__':
    asyncio.run(main())
