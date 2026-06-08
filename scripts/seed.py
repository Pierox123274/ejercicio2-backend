"""Crea datos de ejemplo en Firestore si la colección está vacía."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.config import PERSONAS_COLLECTION
from core.database import get_db
from models.persona import PersonaCreate
from repository import persona_repository

SAMPLE_PERSONAS = [
    PersonaCreate(
        docIdentidad="76512580",
        nombre="Pepito",
        edad=20,
        correo="pepito@gmail.com",
    ),
    PersonaCreate(
        docIdentidad="20603142",
        nombre="Adair",
        edad=18,
        correo="adair@gmail.com",
    ),
]


def main() -> None:
    db = get_db()
    existing = list(db.collection(PERSONAS_COLLECTION).limit(1).stream())

    if existing:
        print("La colección ya tiene datos. No se agregaron ejemplos.")
        return

    for persona in SAMPLE_PERSONAS:
        persona_repository.create_persona(persona)
        print(f"Creada: {persona.nombre} ({persona.docIdentidad})")

    print("Datos de ejemplo listos en Firestore.")


if __name__ == "__main__":
    main()
