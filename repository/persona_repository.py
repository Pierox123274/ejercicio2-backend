from core.config import PERSONAS_COLLECTION
from core.database import get_db
from models.persona import Persona, PersonaCreate, PersonaUpdate


def _doc_to_persona(doc) -> Persona:
    data = doc.to_dict() or {}
    return Persona(
        docIdentidad=doc.id,
        nombre=data["nombre"],
        edad=data["edad"],
        correo=data["correo"],
    )


def list_personas() -> list[Persona]:
    db = get_db()
    docs = db.collection(PERSONAS_COLLECTION).stream()
    personas = [_doc_to_persona(doc) for doc in docs]
    return sorted(personas, key=lambda persona: persona.nombre)


def get_persona(doc_identidad: str) -> Persona | None:
    db = get_db()
    doc = db.collection(PERSONAS_COLLECTION).document(doc_identidad).get()
    return _doc_to_persona(doc) if doc.exists else None


def persona_exists(doc_identidad: str) -> bool:
    db = get_db()
    doc = db.collection(PERSONAS_COLLECTION).document(doc_identidad).get()
    return doc.exists


def create_persona(persona: PersonaCreate) -> Persona:
    db = get_db()
    doc_ref = db.collection(PERSONAS_COLLECTION).document(persona.docIdentidad)
    doc_ref.set(
        {
            "nombre": persona.nombre,
            "edad": persona.edad,
            "correo": persona.correo,
        }
    )
    return Persona(**persona.model_dump())


def update_persona(doc_identidad: str, persona: PersonaUpdate) -> Persona | None:
    db = get_db()
    doc_ref = db.collection(PERSONAS_COLLECTION).document(doc_identidad)
    if not doc_ref.get().exists:
        return None

    doc_ref.update(
        {
            "nombre": persona.nombre,
            "edad": persona.edad,
            "correo": persona.correo,
        }
    )
    return Persona(docIdentidad=doc_identidad, **persona.model_dump())


def delete_persona(doc_identidad: str) -> bool:
    db = get_db()
    doc_ref = db.collection(PERSONAS_COLLECTION).document(doc_identidad)
    if not doc_ref.get().exists:
        return False

    doc_ref.delete()
    return True
