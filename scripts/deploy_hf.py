"""Despliega el backend en Hugging Face Spaces."""

from __future__ import annotations

import json
import os
from pathlib import Path

from huggingface_hub import HfApi, add_space_secret, create_repo, upload_folder

ROOT = Path(__file__).resolve().parent.parent
SPACE_ID = "Pierox123274/ejercicio2-api"
FIREBASE_CONFIG = Path.home() / ".config" / "configstore" / "firebase-tools.json"
CREDENTIALS_FILE = ROOT / "firebase-service-account.json"


def resolve_refresh_token() -> str:
    env_token = os.getenv("FIREBASE_REFRESH_TOKEN", "")
    if env_token:
        return env_token
    if not FIREBASE_CONFIG.exists():
        return ""
    config = json.loads(FIREBASE_CONFIG.read_text(encoding="utf-8"))
    return config.get("tokens", {}).get("refresh_token", "")


def main() -> None:
    api = HfApi(token=os.getenv("HF_TOKEN") or None)
    create_repo(SPACE_ID, repo_type="space", space_sdk="docker", exist_ok=True)

    upload_folder(
        folder_path=str(ROOT),
        repo_id=SPACE_ID,
        repo_type="space",
        ignore_patterns=[
            ".venv",
            "__pycache__",
            "scripts",
            ".env",
            ".env.example",
            ".gitignore",
            ".hf-token",
            "firebase-service-account.json",
            "deploy.ps1",
            "install.ps1",
            ".git",
        ],
    )

    add_space_secret(SPACE_ID, "FIREBASE_PROJECT_ID", "ing-web-93d49")
    add_space_secret(SPACE_ID, "PERSONAS_COLLECTION", "personas")
    add_space_secret(
        SPACE_ID,
        "CORS_ORIGINS",
        "https://ing-web-93d49.web.app,https://ing-web-93d49.firebaseapp.com,http://localhost:4201",
    )

    credentials_json = os.getenv("FIREBASE_CREDENTIALS_JSON", "")
    if credentials_json:
        add_space_secret(SPACE_ID, "FIREBASE_CREDENTIALS_JSON", credentials_json)
    elif CREDENTIALS_FILE.exists():
        add_space_secret(
            SPACE_ID,
            "FIREBASE_CREDENTIALS_JSON",
            CREDENTIALS_FILE.read_text(encoding="utf-8"),
        )
    else:
        refresh_token = resolve_refresh_token()
        if not refresh_token:
            raise SystemExit("Sin credenciales Firebase. Ejecuta: firebase login")
        add_space_secret(SPACE_ID, "FIREBASE_REFRESH_TOKEN", refresh_token)

    print("Backend desplegado en Hugging Face")


if __name__ == "__main__":
    main()
