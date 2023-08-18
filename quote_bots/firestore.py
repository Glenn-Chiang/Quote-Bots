from firebase_admin import initialize_app, firestore, credentials
from google.cloud.firestore import Client


cred = credentials.Certificate(r'C:\Users\glenn\Programming Projects\Quote_Bots\quote_bots\credentials.json')
app = initialize_app(credential=cred)
db: Client = firestore.client()