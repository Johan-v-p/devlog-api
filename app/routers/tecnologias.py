from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.tecnologia import TecnologiaCreate, TecnologiaResponse, TecnologiaUpdate
from app.services.tecnologia_service import crear_tecnologia as crear_tecnologia_service, obtener_tecnologias as obtener_tecnologias_service , obtener_tecnologia_por_id, modificar_tecnologia, remover_tecnologia
from app.core.database import get_db

router = APIRouter(prefix="/tecnologias", tags=["tecnologias"])

@router.get("/", response_model=list[TecnologiaResponse])
def obtener_tecnologias(db: Session = Depends(get_db)):
    return obtener_tecnologias_service(db)

@router.get("/{id}", response_model=TecnologiaResponse)
def obtener_tecnologia(id: int, db: Session = Depends(get_db)):
    return obtener_tecnologia_por_id(id, db)

@router.post("/", response_model=TecnologiaResponse)
def crear_tecnologia(tecnologia: TecnologiaCreate, db: Session = Depends(get_db)):
    return crear_tecnologia_service(tecnologia, db)

@router.put("/{id}", response_model=TecnologiaResponse)
def atualizar_tecnologia(id: int, tecnologia: TecnologiaUpdate, db: Session = Depends(get_db)):
    return modificar_tecnologia(id,db,tecnologia)

@router.delete("/{id}") 
def eliminar_tecnologia(id: int, db: Session = Depends(get_db)):
    return remover_tecnologia(id, db)