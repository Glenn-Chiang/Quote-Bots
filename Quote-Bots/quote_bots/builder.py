from telegram.ext import Application, CommandHandler
from handlers import subscribeHandler, helpHandler, quoteHandler, unsubscribeHandler, subscribersHandler


def build(bot_token: str, author_name: str):
    app = Application.builder().token(bot_token).build()
    app.add_handler(CommandHandler('start', subscribeHandler))
    app.add_handler(CommandHandler('subscribers', subscribersHandler))
    app.add_handler(CommandHandler('help', helpHandler))
    app.add_handler(CommandHandler('quote', quoteHandler))
    app.add_handler(CommandHandler('unsubscribe', unsubscribeHandler))
    app.bot_data["author_name"] = author_name
    return app