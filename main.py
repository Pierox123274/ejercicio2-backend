from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apis.health_router import router as health_router
from apis.persona_router import router as persona_router
from core.config import CORS_ORIGINS

app = FastAPI(title="Ejercicio2 API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_origin_regex=r"https://(.*\.onrender\.com|.*\.web\.app|.*\.firebaseapp\.com|.*\.hf\.space)$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(persona_router)
