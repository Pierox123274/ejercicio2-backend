from fastapi import APIRouter, HTTPException

from models.persona import Persona, PersonaCreate, PersonaUpdate
from services import persona_service

router = APIRouter(prefix="/api/personas", tags=["personas"])


@router.get("", response_model=list[Persona])
def list_personas():
    return persona_service.list_personas()


@router.get("/{doc_identidad}", response_model=Persona)
def get_persona(doc_identidad: str):
    persona = persona_service.get_persona(doc_identidad)
    if persona is None:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    return persona


@router.post("", response_model=Persona, status_code=201)
def create_persona(persona: PersonaCreate):
    return persona_service.create_persona(persona)


@router.put("/{doc_identidad}", response_model=Persona)
def update_persona(doc_identidad: str, persona: PersonaUpdate):
    return persona_service.update_persona(doc_identidad, persona)


@router.delete("/{doc_identidad}", status_code=204)
def delete_persona(doc_identidad: str):
    persona_service.delete_persona(doc_identidad)
