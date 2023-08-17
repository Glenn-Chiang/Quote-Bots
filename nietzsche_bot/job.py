import asyncio
import os
from telegram import Bot
from services import get_random_quote
from dotenv import load_dotenv
from services import get_subscribers
from main import message_admin
load_dotenv()

author_name = 'Friedrich_Nietzsche'

async def main():
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    subscribers = get_subscribers(author_name=author_name)
    quote = get_random_quote(author_name=author_name)

    for subscriber in subscribers:
        try:
            await bot.send_message(chat_id=subscriber["chatId"], text=quote)
            print("Quote sent to subscribers")
        except Exception as err:
            error_message = f"Error sending quote to {subscriber['name']}"
            print(error_message, err)
            await message_admin(bot=bot, message_text=error_message)


def lambda_handler(event, context):
    asyncio.run(main())
    return


if __name__ == '__main__':
    asyncio.run(main())
