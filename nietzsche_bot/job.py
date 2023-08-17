import asyncio
import os
from telegram import Bot
from services import get_random_quote
from dotenv import load_dotenv

load_dotenv('.env')
BASE_URL = os.getenv('BASE_URL')


async def main():
    bot = Bot(token=os.getenv('BOT_TOKEN'))

    users = []
    for user in users:
        await send_quote(bot=bot, author_url_name='Friedrich_Nietzsche', chat_id=user.chat_id)


async def send_quote(bot: Bot, author_url_name: str, chat_id: str):
    quote = get_random_quote(author_name=author_url_name)
    await bot.send_message(chat_id=chat_id, text=quote)


if __name__ == 'main':
    asyncio.run(main())
