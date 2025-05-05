import logging
from utils.settings import SETTINGS
import os

os.makedirs(SETTINGS.LOG_PATH, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(f"{SETTINGS.LOG_PATH}/logs.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
