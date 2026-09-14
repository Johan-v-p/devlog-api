from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.meta_semanal import MetaSemanalCreate, MetaSemanalResponse, MetaSemanalUpdate
from app.services.meta_semanal_service import crear_meta_semanal as crear_meta_semanal_service, obtener_metas_semanal as obtener_metas_semanal_service, obtener_meta_semanal_por_id, modificar_meta_semanal, remover_meta_semanal
from app.core.database import get_db
from app.core.auth_dependency import obtener_usuario_actual

router = APIRouter(prefix="/metas_semanales", tags=["metas_semanales"])

@router.get("/", response_model=list[MetaSemanalResponse])
def obtener_metas_semanal(db : Session = Depends(get_db)):
    return obtener_metas_semanal_service(db)

@router.get("/{id}", response_model=MetaSemanalResponse)
def obtener_meta_semanal(id: int, db: Session = Depends(get_db)):
    return obtener_meta_semanal_por_id(id, db)

@router.post("/", response_model= MetaSemanalResponse)
def crear_meta_semanal(meta_semanal: MetaSemanalCreate, db: Session = Depends(get_db), usuario_id: int = Depends(obtener_usuario_actual)):
    return crear_meta_semanal_service(meta_semanal,usuario_id,db)

@router.put("/{id}", response_model= MetaSemanalResponse)
def atualizar_meta_semanal(id: int, meta_semanal: MetaSemanalUpdate, db: Session = Depends(get_db), usuario_id: int = Depends(obtener_usuario_actual)):
    return modificar_meta_semanal(id,db,meta_semanal)

@router.delete("/{id}")
def eliminar_meta_semanal(id: int, db: Session = Depends(get_db), usuario_id: int = Depends(obtener_usuario_actual)):
    return remover_meta_semanal(id, db)
