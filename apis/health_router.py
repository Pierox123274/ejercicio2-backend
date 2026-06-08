from fastapi import APIRouter, HTTPException

from core.config import FIREBASE_PROJECT_ID, PERSONAS_COLLECTION
from core.database import get_db

router = APIRouter(tags=["health"])


@router.get("/")
@router.get("/api")
def api_root():
    return {
        "service": "Ejercicio2 API",
        "health": "/api/health",
        "personas": "/api/personas",
    }


@router.get("/api/health")
def health():
    try:
        db = get_db()
        list(db.collection(PERSONAS_COLLECTION).limit(1).stream())
    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail=f"No se pudo conectar con Firebase: {exc}",
        ) from exc

    from core.database import get_auth_mode

    return {
        "status": "ok",
        "database": "firebase",
        "project": FIREBASE_PROJECT_ID,
        "auth": get_auth_mode(),
    }
