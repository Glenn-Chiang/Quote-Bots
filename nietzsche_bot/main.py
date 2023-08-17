from telegram import Update, Bot
from telegram.ext import Application, CallbackContext, CommandHandler
import requests
import os
from dotenv import load_dotenv
from services import get_random_quote, register_user, remove_subscriber_from_author

load_dotenv()
BOT_TOKEN = os.environ.get('BOT_TOKEN')
ADMIN_CHAT_ID = os.environ.get('ADMIN_CHAT_ID')
author_name = 'Friedrich_Nietzsche'


async def subscribe(update: Update, context: CallbackContext):
    username = update.effective_user.username
    chat_id = update.effective_chat.id

    user = {"name": username, "chat_id": chat_id}

    # Send post request to quotes API to register user as a subscriber
    try:
        res = register_user(user=user, author_name=author_name)
        if res.status_code == 409:
            raise requests.exceptions.HTTPError(res.json()['error'])

        await update.message.reply_text(text="Subscribed! Type /help for a list of commands")
        await message_admin(
            bot=context.bot, message_text=f"{username} has subscribed to Nietzsche Bot!")
        print(f"{username} has subscribed to Nietzsche Bot")

    except Exception as err:
        print(f'Error registering {username}:', err, sep='\n')

        await update.message.reply_text(text=f"{err}")

        await message_admin(bot=context.bot,
                            message_text=f"Error registering {username}")


async def send_random_quote(update: Update, context: CallbackContext):
    try:
        quote = get_random_quote(author_name=author_name)
        await update.message.reply_text(text=quote)

    except Exception as err:
        print('Error getting quote:', err)

        await update.message.reply_text(text="Error getting quote")

        await message_admin(bot=context.bot, message_text=f"Error getting quote")


async def help(update: Update, context: CallbackContext):
    help_message = """
/random  -  Get a random quote
/unsubscribe  -  Stop receiving daily quotes
"""
    await update.message.reply_text(text=help_message)


async def unsubscribe(update: Update, context: CallbackContext):
    username = update.effective_user.username
    res = remove_subscriber_from_author(username=username, author_name=author_name)
    await update.message.reply_text(text="Unsubscribed. To subscribe again, enter /start")
    await message_admin(bot=context.bot, message_text=f"{username} has unsubscribed")


async def message_admin(bot: Bot, message_text: str):
    await bot.send_message(chat_id=ADMIN_CHAT_ID, text=message_text)


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler('start', subscribe))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('random', send_random_quote))
    app.add_handler(CommandHandler('unsubscribe', unsubscribe))

    print('Bot started. Polling for updates...')
    app.run_polling()


if __name__ == '__main__':
    main()
