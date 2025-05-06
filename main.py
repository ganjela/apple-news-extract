from extract import extract
from utils.settings import SETTINGS
from utils.logger import logger

def main(request):
    request = request.get_json()
    extract(SETTINGS.API_URL, SETTINGS.PARAMS)
    logger.info("Data extraction completed successfully")
    return {
        "message": "Data extraction completed successfully",
        "status": "success"
    }
