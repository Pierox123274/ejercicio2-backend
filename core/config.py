import json
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

BASE_DIR = Path(__file__).resolve().parent.parent
FIREBASE_PROJECT_ID = os.getenv("FIREBASE_PROJECT_ID", "ing-web-93d49")
PERSONAS_COLLECTION = os.getenv("PERSONAS_COLLECTION", "personas")
FIREBASE_CREDENTIALS_JSON = os.getenv("FIREBASE_CREDENTIALS_JSON", "")
FIREBASE_REFRESH_TOKEN = os.getenv("FIREBASE_REFRESH_TOKEN", "")
FIREBASE_CREDENTIALS_PATH = os.getenv(
    "FIREBASE_CREDENTIALS_PATH", str(BASE_DIR / "firebase-service-account.json")
)
CORS_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "CORS_ORIGINS",
        "http://localhost:4200,http://localhost:4201,https://ing-web-93d49.web.app,https://ing-web-93d49.firebaseapp.com,https://pierox123274-ejercicio2-api.hf.space",
    ).split(",")
    if origin.strip()
]


def resolve_credentials_path() -> Path:
    if FIREBASE_CREDENTIALS_JSON:
        credentials_path = BASE_DIR / ".firebase-credentials.json"
        credentials_data = json.loads(FIREBASE_CREDENTIALS_JSON)
        credentials_path.write_text(
            json.dumps(credentials_data),
            encoding="utf-8",
        )
        return credentials_path

    credentials_path = Path(FIREBASE_CREDENTIALS_PATH)
    if not credentials_path.is_absolute():
        credentials_path = BASE_DIR / credentials_path
    return credentials_path
