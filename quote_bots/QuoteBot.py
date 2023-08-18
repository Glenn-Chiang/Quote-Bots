from telegram.ext import Application, CommandHandler
from quote_bots.handlers import subscribeHandler, helpHandler, quoteHandler, unsubscribeHandler, subscribersHandler


class QuoteBot():
    def __init__(self, app: Application, author_name: str) -> None:
        self.app = app
        self.app.add_handler(CommandHandler('start', subscribeHandler))
        self.app.add_handler(CommandHandler('subscribers', subscribersHandler))
        self.app.add_handler(CommandHandler('help', helpHandler))
        self.app.add_handler(CommandHandler('quote', quoteHandler))
        self.app.add_handler(CommandHandler('unsubscribe', unsubscribeHandler))
        self.app.bot_data["author_name"] = author_name
