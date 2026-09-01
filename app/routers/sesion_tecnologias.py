from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.sesion_tecnologia import SesionTecnologiaCreate, SesionTecnologiaResponse, SesionTecnologiaUpdate
from app.services.sesion_tecnologia_service import crear_sesion_tecnologia as crear_sesion_tecnologia_service, obtener_sesion_tecnologias as obtener_sesion_tecnologias_service, obtener_sesion_tecnologia_por_id, modificar_sesion_tecnologia, remover_sesion_tecnologia
from app.core.database import get_db

router = APIRouter(prefix="/sesion_tecnologias", tags=["sesion_tecnologias"])

@router.get("/", response_model=list[SesionTecnologiaResponse])
def obtener_sesion_tecnologias(db: Session = Depends(get_db)):
    return obtener_sesion_tecnologias_service(db)

@router.get("/{id}", response_model=SesionTecnologiaResponse)
def obtener_sesion_tecnologia(id: int, db: Session = Depends(get_db)):
    return obtener_sesion_tecnologia_por_id(id,db)

@router.post("/", response_model=SesionTecnologiaResponse)
def crear_sesion_tecnologia(sesion_tecnologia: SesionTecnologiaCreate, db: Session = Depends(get_db)):
    return crear_sesion_tecnologia_service(sesion_tecnologia, db)

@router.put("/{id}", response_model=SesionTecnologiaResponse)
def atualizar_sesion_tecnologia(id: int, sesion_tecnologia : SesionTecnologiaUpdate, db: Session = Depends(get_db)):
    return modificar_sesion_tecnologia(id,db,sesion_tecnologia)

@router.delete("/{id}")
def eliminar_sesion_tecnologia(id: int, db: Session = Depends(get_db)):
    return remover_sesion_tecnologia(id, db)


