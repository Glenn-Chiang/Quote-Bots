from quote_bots.send_quote import send_quote
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

async def main():
    await send_quote(author_name='Friedrich_Nietzsche', bot_token=os.getenv('BOT_TOKEN'))

def lambda_handler(event, context):
    asyncio.run(main())

if __name__=='__main__':
    asyncio.run(main())
