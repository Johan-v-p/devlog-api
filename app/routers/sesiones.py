from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.sesion import SesionCreate, SesionResponse, SesionUpdate
from app.services.sesion_service import crear_sesion as crear_sesion_service, obtener_sesion_por_id, obtener_sesiones as obtener_sesiones_service, modificar_sesion, remover_sesion
from app.core.database import get_db

router = APIRouter(prefix="/sesiones", tags=["sesiones"])

@router.get("/", response_model=list[SesionResponse])
def obtener_sesiones(db: Session = Depends(get_db)):
    return obtener_sesiones_service(db)

@router.get("/{id}", response_model=SesionResponse)
def obtener_sesion(id: int, db: Session = Depends(get_db)):
    return obtener_sesion_por_id(id, db)

@router.post("/", response_model=SesionResponse)
def crear_sesion(sesion: SesionCreate, db: Session = Depends(get_db)):
    return crear_sesion_service(sesion,1,db)

@router.put("/{id}", response_model= SesionResponse)
def atualizar_sesion(id: int, sesion: SesionUpdate, db: Session = Depends(get_db)):
    return modificar_sesion(id,db,sesion)

@router.delete("/{id}")
def eliminar_sesion(id: int, db: Session = Depends(get_db)):
    return remover_sesion(id, db)
