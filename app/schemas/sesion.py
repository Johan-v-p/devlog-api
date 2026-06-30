from pydantic import BaseModel, Field
from datetime import date

class SesionCreate(BaseModel):
    fecha: date
    horas_totales: float = Field(gt=0, le=24)
    nivel_energia: int = Field(ge=1, le=5)
    notas: str | None = None

class SesionUpdate(BaseModel):
    fecha: date | None = None
    horas_totales: float | None = Field(default=None, gt=0, le=24)
    nivel_energia: int | None = Field(default=None, ge=1, le=5)
    notas: str | None = None

class SesionResponse(BaseModel):
    id: int
    usuario_id: int
    fecha: date
    horas_totales: float
    nivel_energia: int
    notas: str | None = None

