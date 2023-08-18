from firebase_admin import initialize_app, firestore, credentials
from google.cloud.firestore import Client

cred = credentials.Certificate('./credentials.json')
app = initialize_app(credential=cred)
db: Client = firestore.client()