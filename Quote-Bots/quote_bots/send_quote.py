from telegram import Bot
from quote_bots.services import get_random_quote, get_subscribers


async def send_quote_to_user(author_name: str, bot: Bot):
    subscribers = get_subscribers(author_name=author_name)
    quote = get_random_quote(author_name=author_name)

    for subscriber in subscribers:
        await bot.send_message(chat_id=subscriber["chatId"], text=quote)

    print("Quote sent to subscribers")
    

CHANNEL_ID = '@philosopher_quotes'
async def send_quote_to_channel(author_name: str, bot: Bot):
    quote = get_random_quote(author_name=author_name)
    await bot.send_message(chat_id=CHANNEL_ID, text=quote)
