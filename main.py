from extract import extract
from utils.settings import SETTINGS
from utils.logger import logger
from firestore import Firestore

def main(request):

    missing_dates = request.get_json()["missing_dates"]
    logger.info(f"Received request: {request}")

    for date in missing_dates:
        docs = extract(SETTINGS.API_URL, {
            "from": date,
            "to": date,
            "apiKey": SETTINGS.API_KEY
        })
        Firestore().upload_docs(docs["articles"], date)

    logger.info("Data extraction completed successfully")
    return {
        "message": "Data extraction completed successfully",
        "status": "success"
    }