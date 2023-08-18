import requests
import os
from dotenv import load_dotenv
from firestore import db
from google.cloud.firestore_v1.document import DocumentReference
from google.cloud.firestore_v1.collection import CollectionReference

load_dotenv()
BASE_URL = os.getenv('BASE_URL')


def get_random_quote(author_name: str):
    response = requests.get(
        f'{BASE_URL}/authors/{author_name}/randomquote')
    quote_content = response.json()['content']
    full_quote = f"{quote_content}"
    return full_quote


def register_user(author_name: str, user: dict):
    subscribers_collection: CollectionReference = db.collection(
        "authors").document(author_name).collection("subscribers")
    subscriber_doc: DocumentReference = subscribers_collection.document(document_id=user["chat_id"])
    subscriber_doc.set(document_data=user)
    # If user is already subscribed, nothing will happen

def get_subscribers(author_name: str) -> list:
    # response = requests.get(f"{BASE_URL}/authors/{author_name}/subscribers")
    # subscribers = response.json()
    subscribers = [{"chatId": "5291406801"}, {"name": "Glenn_Chiang"}]
    return subscribers


def remove_subscriber_from_author(author_name: str, username: str):
    response = requests.delete(
        f"{BASE_URL}/authors/{author_name}/subscribers/{username}")
    return response
