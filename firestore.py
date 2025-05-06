from google.cloud import firestore
from  utils.settings import SETTINGS

db = firestore.Client()

class Firestore:
    def __init__(self):
        self.db = firestore.Client(database=SETTINGS.FIRESTORE_DB)
        self.collection = self.db.collection(SETTINGS.FIRESTORE_COLLECTION)

    def upload_docs(self, docs):
        for doc in docs:
            self.collection.add(doc)

