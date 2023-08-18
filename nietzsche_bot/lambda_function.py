import asyncio
from send_quote import send_quote
import os
from dotenv import load_dotenv
load_dotenv()

def lambda_handler(event, context):
    asyncio.run(send_quote(author_name='Friedrich_Nietzsche', bot_token=os.getenv('BOT_TOKEN')))
    return
