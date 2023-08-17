import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL')


def get_random_quote(author_name: str) -> str:
    response = requests.get(
        f'{BASE_URL}/authors/{author_name}/randomquote')
    quote_content = response.json()['content']
    full_quote = f"{quote_content}"
    return full_quote


def register_user(author_name: str, user: dict):
    requests.post(
        f"{BASE_URL}/authors/{author_name}/subscribers", json=user)
