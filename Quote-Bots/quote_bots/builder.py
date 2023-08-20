from telegram.ext import Application, CommandHandler
from quote_bots.handlers import subscribeHandler, helpHandler, quoteHandler, unsubscribeHandler, subscribersHandler


def build(bot_token: str, author_name: str, admin_chat_id: str):
    app = Application.builder().token(bot_token).build()
    app.add_handler(CommandHandler('start', subscribeHandler))
    app.add_handler(CommandHandler('subscribers', subscribersHandler))
    app.add_handler(CommandHandler('help', helpHandler))
    app.add_handler(CommandHandler('quote', quoteHandler))
    app.add_handler(CommandHandler('unsubscribe', unsubscribeHandler))
    app.bot_data["author_name"] = author_name
    app.bot_data["admin_chat_id"] = admin_chat_id
    return app
