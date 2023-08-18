from telegram import Bot
from services import get_random_quote
from services import get_subscribers


async def send_quote(author_name: str, bot_token: str):
    bot = Bot(token=bot_token)
    subscribers = get_subscribers(author_name=author_name)
    quote = get_random_quote(author_name=author_name)

    for subscriber in subscribers:
        try:
            await bot.send_message(chat_id=subscriber["chatId"], text=quote)
            print("Quote sent to subscribers")
        except Exception as err:
            error_message = f"Error sending quote to {subscriber['name']}"
            print(error_message, err)



