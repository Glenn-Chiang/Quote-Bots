import asyncio
import os
import requests
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

async def main():
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    
    users = []
    for user in users:
        await send_quote(bot=bot, author_url_name='Friedrich_Nietzsche', chat_id=user.chat_id)


async def send_quote(bot: Bot, author_url_name: str, chat_id: str):
    response = requests.get(
        f'${BASE_URL}/authors/${author_url_name}/randomquote')

    quote_content: str = response.json().content
    author_name: str = response.json().author.name
    full_quote = f"{quote_content}\n\n- {author_name}"

    await bot.send_message(chat_id=chat_id, text=full_quote)


    

if __name__ == 'main':
    asyncio.run(main())
