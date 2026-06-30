from pydantic import BaseModel, Field
from datetime import date

class MetaSemanalCreate(BaseModel):
    titulo: str = Field(max_length=150)
    descripcion: str | None = None
    objetivo_horas: int = Field(gt=0, le=168)
    fecha_inicio: date
    fecha_fin: date
    completada: bool = False

class MetaSemanalUpdate(BaseModel):
    titulo: str | None = Field(default= None, max_length=150)
    descripcion: str | None = None
    objetivo_horas: int | None = Field(default=None, gt=0, le=168)
    fecha_inicio: date | None = None
    fecha_fin: date | None = None
    completada: bool | None = None

class MetaSemanalResponse(BaseModel):
    id: int
    usuario_id: int
    titulo: str
    descripcion: str | None = None
    objetivo_horas: int
    fecha_inicio: date
    fecha_fin: date
    completada: bool = False