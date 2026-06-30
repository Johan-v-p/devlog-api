from pydantic import BaseModel, Field

class SesionTecnologiaCreate(BaseModel):
    sesion_id: int
    tecnologia_id: int
    horas: float = Field(gt=0, le=24)

class SesionTecnologiaUpdate(BaseModel):
    horas: float | None = Field(default=None, gt=0, le=24)

class SesionTecnologiaResponse(BaseModel):
    id: int
    sesion_id: int
    tecnologia_id: int
    horas: float