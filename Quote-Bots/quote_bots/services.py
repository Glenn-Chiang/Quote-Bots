import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL')


def get_random_quote(author_name: str):
    response = requests.get(
        f'{BASE_URL}/authors/{author_name}/randomquote')
    response.raise_for_status()
    quote_content = response.json()['content']
    full_quote = f"{quote_content}"
    return full_quote


def subscribe(author_name: str, user: dict):
    response = requests.post(f'{BASE_URL}/authors/{author_name}/subscribers', json=user)
    response.raise_for_status()


def get_subscribers(author_name: str) -> list:
    response = requests.get(f'{BASE_URL}/authors/{author_name}/subscribers')
    response.raise_for_status()
    return response.json()

def unsubscribe(author_name: str, chat_id: str):
    response = requests.delete(f'{BASE_URL}/authors/{author_name}/subscribers/{chat_id}')
    response .raise_for_status()
