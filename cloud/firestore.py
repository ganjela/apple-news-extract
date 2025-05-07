from google.cloud import firestore
from utils.settings import SETTINGS


class Firestore:
    def __init__(self):
        self.db = firestore.Client(database=SETTINGS.FIRESTORE_DB)

    def upload_docs(self, docs, date):
        for doc in docs:
            self.db.collection(date).add(doc)
