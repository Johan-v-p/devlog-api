from pydantic import BaseModel, Field

class TecnologiaCreate(BaseModel):
    nombre: str = Field(max_length=100)

class TecnologiaUpdate(BaseModel):
    nombre: str | None = Field(default=None, max_length=100)

class TecnologiaResponse(BaseModel):
    id: int
    nombre: str