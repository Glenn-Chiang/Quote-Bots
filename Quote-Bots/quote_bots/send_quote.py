from telegram import Bot
from quote_bots.services import get_random_quote, get_subscribers


async def send_quote(author_name: str, bot_token: str):
    bot = Bot(token=bot_token)
    subscribers = get_subscribers(author_name=author_name)
    quote = get_random_quote(author_name=author_name)

    for subscriber in subscribers:
        await bot.send_message(chat_id=subscriber["chatId"], text=quote)

    print("Quote sent to subscribers")
    



