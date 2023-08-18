import os
from telegram import Update, Bot
from telegram.ext import CallbackContext
from dotenv import load_dotenv
load_dotenv()
from quote_bots.services import get_random_quote, subscribe, unsubscribe


async def subscribeHandler(update: Update, context: CallbackContext):
    author_name = context.bot_data["author_name"]
    username = update.effective_user.username
    chat_id = update.effective_chat.id

    user = {"name": username, "chat_id": chat_id}

    subscribe(user=user, author_name=author_name)

    await update.message.reply_text(text="Subscribed! Type /help for a list of commands")
    await message_admin(
        bot=context.bot, message_text=f"{username} has subscribed to Nietzsche Bot!")


async def quoteHandler(update: Update, context: CallbackContext):
    author_name = context.bot_data["author_name"]
    try:
        quote = get_random_quote(author_name=author_name)
        await update.message.reply_text(text=quote)

    except Exception as err:
        print('Error getting quote:', err)

        await update.message.reply_text(text="Error getting quote")

        await message_admin(bot=context.bot, message_text=f"Error getting quote")


async def helpHandler(update: Update, context: CallbackContext):
    help_message = """
/random  -  Get a random quote
/unsubscribe  -  Stop receiving daily quotes
"""
    await update.message.reply_text(text=help_message)


async def unsubscribeHandler(update: Update, context: CallbackContext):
    author_name = context.bot_data["author_name"]
    username = update.effective_user.username
    chat_id = str(update.effective_chat.id)
    unsubscribe(author_name=author_name, chat_id=chat_id)
    await update.message.reply_text(text="Unsubscribed. To subscribe again, enter /start")
    await message_admin(bot=context.bot, message_text=f"{username} has unsubscribed")


async def message_admin(bot: Bot, message_text: str):
    await bot.send_message(chat_id=os.getenv('ADMIN_CHAT_ID'), text=message_text)
