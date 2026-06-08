from fastapi import HTTPException

from models.persona import Persona, PersonaCreate, PersonaUpdate
from repository import persona_repository


def list_personas() -> list[Persona]:
    return persona_repository.list_personas()


def get_persona(doc_identidad: str) -> Persona | None:
    return persona_repository.get_persona(doc_identidad)


def create_persona(persona: PersonaCreate) -> Persona:
    if persona_repository.persona_exists(persona.docIdentidad):
        raise HTTPException(
            status_code=409,
            detail="Ya existe una persona con ese documento de identidad",
        )
    return persona_repository.create_persona(persona)


def update_persona(doc_identidad: str, persona: PersonaUpdate) -> Persona:
    updated = persona_repository.update_persona(doc_identidad, persona)
    if updated is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return updated


def delete_persona(doc_identidad: str) -> None:
    deleted = persona_repository.delete_persona(doc_identidad)
    if not deleted:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
