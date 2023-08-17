from telegram import Update, Bot
from telegram.ext import Application, CallbackContext, CommandHandler
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv('.env')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
load_dotenv('../.env')
BASE_URL = os.environ.get('BASE_URL')
ADMIN_CHAT_ID = os.environ.get('ADMIN_CHAT_ID')


async def register_user(update: Update, context: CallbackContext):
    username = update.effective_user.username
    chat_id = update.effective_chat.id

    user = {"name": username, "chat_id": chat_id}
    user_data = json.dumps(user)

    # Send post request to quotes API to register user as a subscriber
    try:
        requests.post(
            f"{BASE_URL}/authors/Friedrich_Nietzsche/subscribers", json=user_data)
        await update.message.reply_text(text="Registration successful")
        await message_admin(
            bot=context.bot, message_text=f"{username} has subscribed to Nietzsche Bot!")

    except Exception as err:
        print('Error registering user:', err)
        await message_admin(bot=context.bot,
                      message_text=f"Error registering {username}")


async def message_admin(bot: Bot, message_text: str):
    await bot.send_message(chat_id=ADMIN_CHAT_ID, text=message_text)


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', register_user))
    print('Bot started. Polling for updates...')
    app.run_polling()


if __name__ == '__main__':
    main()
