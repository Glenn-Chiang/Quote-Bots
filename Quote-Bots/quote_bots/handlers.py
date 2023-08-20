from services import get_random_quote, subscribe, unsubscribe, get_subscribers
import requests
from telegram import Update, Bot
from telegram.ext import CallbackContext
from dotenv import load_dotenv
load_dotenv()


async def quoteHandler(update: Update, context: CallbackContext):
    author_name = context.bot_data["author_name"]
    try:
        quote = get_random_quote(author_name=author_name)
        await update.message.reply_text(text=quote)

    except requests.exceptions.HTTPError as error:
        await update.message.reply_text(error["error"])


async def helpHandler(update: Update, context: CallbackContext):
    help_message = """
/random  -  Get a random quote
/unsubscribe  -  Stop receiving daily quotes
"""
    await update.message.reply_text(text=help_message)


async def subscribersHandler(update: Update, context: CallbackContext):
    author_name = context.bot_data["author_name"]

    try:
        subscribers = get_subscribers(author_name=author_name)
    except requests.exceptions.HTTPError as error:
        await update.message.reply_text(error["error"])

    formatted_subscribers = ('\n').join(
        [subscriber['username'] for subscriber in subscribers])

    await update.message.reply_text(text=formatted_subscribers)


async def subscribeHandler(update: Update, context: CallbackContext):
    author_name = context.bot_data["author_name"]
    username = update.effective_user.username
    chat_id = str(update.effective_chat.id)

    user = {"username": username, "chat_id": chat_id}

    try:
        subscribe(user=user, author_name=author_name)
        await update.message.reply_text(text="Subscribed! Type /help for a list of commands")

        bot: Bot = context.bot
        admin_chat_id = context.bot_data['admin_chat_id']
        bot.send_message(chat_id=admin_chat_id,
                         text=f"{username} has subscribed to Nietzsche Bot!")

    except requests.exceptions.HTTPError as error:
        await update.message.reply_text(error["error"])


async def unsubscribeHandler(update: Update, context: CallbackContext):
    author_name = context.bot_data["author_name"]
    username = update.effective_user.username
    chat_id = str(update.effective_chat.id)

    try:
        unsubscribe(author_name=author_name, chat_id=chat_id)
        await update.message.reply_text(text="Unsubscribed. To subscribe again, enter /start")
        bot: Bot = context.bot
        admin_chat_id = context.bot_data['admin_chat_id']
        await bot.send_message(chat_id=admin_chat_id, text=f"{username} has unsubscribed")

    except requests.exceptions.HTTPError as error:
        await update.message.reply_text(error["error"])
