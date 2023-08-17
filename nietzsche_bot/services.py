import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL')


def get_random_quote(author_name: str):
    response = requests.get(
        f'{BASE_URL}/authors/{author_name}/randomquote')
    quote_content = response.json()['content']
    full_quote = f"{quote_content}"
    return full_quote


def register_user(author_name: str, user: dict):
    response = requests.post(
        f"{BASE_URL}/authors/{author_name}/subscribers", json=user)
    return response

def get_subscribers(author_name: str) -> list:
    response = requests.get(f"{BASE_URL}/authors/{author_name}/subscribers")
    subscribers = response.json()
    return subscribers