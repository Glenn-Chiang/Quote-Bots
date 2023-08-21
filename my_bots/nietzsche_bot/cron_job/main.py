from quote_bots.send_quote import send_quote_to_user, send_quote_to_channel
from telegram import Bot
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

async def main():
    bot = Bot(token=os.getenv('BOT_TOKEN'))
    await send_quote_to_channel(author_name='Friedrich_Nietzsche', bot=bot)
    await send_quote_to_user(author_name='Friedrich_Nietzsche', bot=bot)

def lambda_handler(event, context):
    asyncio.run(main())

if __name__=='__main__':
    asyncio.run(main())
