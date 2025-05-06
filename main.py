from extract import extract
from utils.settings import SETTINGS
from utils.logger import logger
from firestore import Firestore

def main(request):
    if request:
        request = request.get_json()
        logger.info(f"Received request: {request}")

    data = extract(SETTINGS.API_URL, SETTINGS.PARAMS)
    Firestore().upload_docs(data["articles"])
    logger.info("Data extraction completed successfully")
    return {
        "message": "Data extraction completed successfully",
        "status": "success"
    }

