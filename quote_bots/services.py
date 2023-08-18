import requests
import os
from dotenv import load_dotenv
from google.cloud.firestore_v1.document import DocumentReference
from google.cloud.firestore_v1.collection import CollectionReference
from quote_bots.firestore import db

load_dotenv()
BASE_URL = os.getenv('BASE_URL')


def get_random_quote(author_name: str):
    response = requests.get(
        f'{BASE_URL}/authors/{author_name}/randomquote')
    quote_content = response.json()['content']
    full_quote = f"{quote_content}"
    return full_quote


def subscribe(author_name: str, user: dict):
    subscribers_collection: CollectionReference = db.collection(
        "authors").document(author_name).collection("subscribers")
    subscriber_doc: DocumentReference = subscribers_collection.document(
        document_id=user["chat_id"])
    subscriber_doc.set(document_data=user)
    # If user is already subscribed, nothing will happen


def get_subscribers(author_name: str) -> list:
    subscribers_collection: CollectionReference = db.collection(
        "authors").document(author_name).collection("subscribers")
    subscribers = subscribers_collection.get()
    return subscribers


def unsubscribe(author_name: str, chat_id: str):
    subscribers_collection: CollectionReference = db.collection(
        "authors").document(author_name).collection("subscribers")
    subscriber_doc: DocumentReference = subscribers_collection.document(document_id=chat_id)
    subscriber_doc.delete()
