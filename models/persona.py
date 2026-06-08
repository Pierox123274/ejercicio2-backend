from pydantic import BaseModel, EmailStr, Field


class Persona(BaseModel):
    docIdentidad: str = Field(max_length=12)
    nombre: str = Field(max_length=60)
    edad: int
    correo: EmailStr


class PersonaCreate(BaseModel):
    docIdentidad: str = Field(max_length=12)
    nombre: str = Field(max_length=60)
    edad: int
    correo: EmailStr


class PersonaUpdate(BaseModel):
    nombre: str = Field(max_length=60)
    edad: int
    correo: EmailStr
