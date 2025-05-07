
import uuid
from abc import abstractmethod
from concurrent.futures import ThreadPoolExecutor
from utils.logger import logger
import requests
from google.cloud import storage

from utils.settings import SETTINGS


class GCSUploader:
    def __init__(self):
        self.client = storage.Client()
        self.bucket = self.client.bucket(SETTINGS.BUCKET_NAME)
        self.max_workers = SETTINGS.MAX_WORKERS

    @abstractmethod
    def upload(self, data):
        pass

    def _upload_to_bucket(self, content, content_type, destination):
        blob = self.bucket.blob(destination)
        blob.upload_from_string(content, content_type=content_type)
        return destination

class AppleImagesUploader(GCSUploader):
    def __init__(self):
        super().__init__()

        adapter = requests.adapters.HTTPAdapter(
            pool_connections=128,
            pool_maxsize=128,
            max_retries=3,
            pool_block=True
        )
        self.client._http.mount("https://", adapter)
        self.client._http._auth_request.session.mount("https://", adapter)

    def upload(self, data):
        self._upload_images(data)

    def _upload_images(self, data):
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            executor.map(self._upload_image, data)

    def _upload_image(self, data):
        author, url = data["author"], data["urlToImage"]
        with requests.get(url) as response:
            content, content_type = response.content, response.headers.get("Content-Type").split("/")[1]
            destination = f"{author}/{uuid.uuid4()}.{content_type}"
            self._upload_to_bucket(content, content_type, destination)










