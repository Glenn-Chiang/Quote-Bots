from quote_bots.builder import build as build_bot
from telegram import Update
import asyncio
import json
import os
from dotenv import load_dotenv
load_dotenv()


def lambda_handler(event, context):
    asyncio.run(main(event))


async def main(event):
    app = build_bot(bot_token=os.getenv('BOT_TOKEN'),
                    author_name='Friedrich_Nietzsche',
                    admin_chat_id=os.getenv('ADMIN_CHAT_ID'))
    await app.initialize()
    update = Update.de_json(json.loads(event['body']), app.bot)
    await app.process_update(update=update)