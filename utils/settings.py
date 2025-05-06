from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

from secret_manager import SecretManager
from datetime import datetime

load_dotenv()


class Settings(BaseSettings):
    secret_manager: SecretManager = SecretManager()

    API_URL: str
    CURRENT_DATE: str = datetime.now().strftime("%Y-%m-%d")
    API_KEY: str = secret_manager.get_secret("news_api_key")

    PARAMS: dict = {
        "from": CURRENT_DATE,
        "to": CURRENT_DATE,
        "apiKey": API_KEY
    }

    FIRESTORE_COLLECTION: str
    FIRESTORE_DB: str

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

SETTINGS = Settings()