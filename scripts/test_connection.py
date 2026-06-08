"""Verifica la conexión con Firestore del proyecto ing-web-93d49."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.config import FIREBASE_PROJECT_ID, PERSONAS_COLLECTION
from core.database import get_auth_mode, get_db


def main() -> None:
    print(f"Proyecto: {FIREBASE_PROJECT_ID}")
    print(f"Colección: {PERSONAS_COLLECTION}")

    db = get_db()
    print(f"Autenticación: {get_auth_mode()}")

    docs = list(db.collection(PERSONAS_COLLECTION).limit(5).stream())
    print(f"Conexión OK. Documentos en '{PERSONAS_COLLECTION}': {len(docs)}")

    for doc in docs:
        print(f"  - {doc.id}: {doc.to_dict()}")


if __name__ == "__main__":
    main()
