from telegram.ext import Application
from quote_bots.QuoteBot import QuoteBot
import os
from dotenv import load_dotenv
load_dotenv()


def main():
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    app = Application.builder().token(BOT_TOKEN).build()
    nietzsche_bot = QuoteBot(app=app, author_name="Friedrich_Nietzsche")
    print('Running Nietzsche Bot...')
    nietzsche_bot.app.run_polling()

if __name__ == '__main__':
    main()