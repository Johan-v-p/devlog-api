from app.schemas.meta_semanal import MetaSemanalCreate, MetaSemanalUpdate
from app.models.meta_semanal import MetasSemanal
from app.repositories.meta_semanal_repo import crear_meta_semanal as guardar_meta_semanal, atualizar_meta_semanal, obtener_meta_semanal_por_id as ver_meta_semanal_por_id, obtener_metas_semanal as ver_metas_semanal, eliminar_meta_semanal
from sqlalchemy.orm import Session
from fastapi import HTTPException


    
def crear_meta_semanal(meta_semanal: MetaSemanalCreate,usuario_id: int, db:Session):
    datos_meta_semanal = meta_semanal.model_dump()
    datos_meta_semanal["usuario_id"] = usuario_id
    nueva_meta_semanal = MetasSemanal(**datos_meta_semanal)
    return guardar_meta_semanal(db, nueva_meta_semanal)

def obtener_metas_semanal(db: Session):
    metas_semanal = ver_metas_semanal(db)
    return metas_semanal

def obtener_meta_semanal_por_id(id: int, db: Session):
    meta_semanal = ver_meta_semanal_por_id(db, id)
    if not meta_semanal:
        raise HTTPException(status_code=404, detail="La meta semanal no existe")
    return meta_semanal

def modificar_meta_semanal(id: int,db: Session,meta_semanal_db: MetaSemanalUpdate):
    meta_semanal = ver_meta_semanal_por_id(db, id)
    if not meta_semanal:
        raise HTTPException(status_code=404, detail="La meta semanal no existe")
    datos_nuevos = meta_semanal_db.model_dump(exclude_unset=True)
    datos_atualizados = atualizar_meta_semanal(db,id,datos_nuevos)
    return datos_atualizados

def remover_meta_semanal(id: int,db: Session):
    meta_semanal = ver_meta_semanal_por_id(db, id)
    if not meta_semanal:
        raise HTTPException(status_code=404, detail="La meta semanal no existe")
    eliminar_meta_semanal(db, id)
    return {"mensaje": "meta semanal eliminada con exito"}