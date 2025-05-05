from extract import extract
from utils.settings import SETTINGS
from utils.logger import logger

def main(request):
    try:
        request = request.get_json()
        extract(SETTINGS.API_URL, SETTINGS.PARAMS)
        logger.info("Data extraction completed successfully")
    except Exception as e:
        logger.error(f"Error occurred during data extraction: {e}")

