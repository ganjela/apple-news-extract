from dotenv import load_dotenv
from google.cloud import secretmanager
import os

load_dotenv()

class SecretManager:
    def __init__(self):
        self.client = secretmanager.SecretManagerServiceClient()
        self.project_id = os.getenv("PROJECT_ID")

    def get_secret(self, secret_id, version_id="latest"):
        name = f"projects/{self.project_id}/secrets/{secret_id}/versions/{version_id}"
        response = self.client.access_secret_version(request={"name": name})
        return response.payload.data.decode("UTF-8")
