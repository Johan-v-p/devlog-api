from pydantic import BaseModel, EmailStr
from datetime import datetime

class UsuarioCreate(BaseModel):
    nombre: str
    email: EmailStr
    password: str


class UsuarioUpdate(BaseModel):
    nombre: str | None = None
    email: EmailStr | None = None
    password: str | None = None

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    email: EmailStr
    creado_en: datetime