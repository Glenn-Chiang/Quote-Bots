import asyncio
import os
import requests
from telegram import Bot
from dotenv import load_dotenv


async def main():
    bot = Bot(token=os.getenv('TOKEN'))

    users = []
    for user in users:
        await send_quote(bot=bot, author_url_name='Friedrich_Nietzsche', chat_id=user.chat_id)


async def send_quote(bot: Bot, author_url_name: str, chat_id: str):
    response = requests.get(
        f'${QUOTES_BASE_URL}/authors/${author_url_name}/randomquote')

    quote_content: str = response.json().content
    author_name: str = response.json().author.name
    full_quote = f"{quote_content}\n\n- {author_name}"

    await bot.send_message(chat_id=chat_id, text=full_quote)


def register_user():
    ...


if __name__ == 'main':
    load_dotenv()
    QUOTES_BASE_URL = os.getenv('QUOTES_BASE_URL')
    USERS_BASE_URL = os.getenv('USERS_BASE_URL')
    asyncio.run(main())
