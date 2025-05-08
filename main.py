from cloud.firestore import Firestore
from cloud.gcstorage import AppleImagesUploader
from extract import extract
from utils.logger import logger
from utils.settings import SETTINGS


def main(request):
    missing_dates = request.get_json()["missing_dates"]
    logger.info(f"Received request: {request}")

    articles = []
    for date in missing_dates:
        docs = extract(SETTINGS.API_URL, {
            "from": date,
            "to": date,
            "apiKey": SETTINGS.API_KEY
        })

        articles.extend(docs["articles"])
        AppleImagesUploader().upload(docs["articles"])
        logger.info("Images uploaded successfully to Google Cloud Storage")
        Firestore().upload_docs(docs["articles"], date)
        logger.info("Documents uploaded successfully to Firestore")

    logger.info("Data extraction completed successfully")
    return {
        "articles": articles,
    }
