import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("path/to/your/firebase-key.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def store_in_firestore(data):
    doc_ref = db.collection('transcriptions').document()
    doc_ref.set(data)
    return doc_ref.id
