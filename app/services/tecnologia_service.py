from app.schemas.tecnologia import TecnologiaCreate, TecnologiaUpdate
from app.models.tecnologia import Tecnologia
from app.repositories.tecnologia_repo import crear_tecnologia as guardar_tecnologia, atualizar_tecnologia, obtener_tecnologia_por_id as ver_tecnologia_por_id, obtener_tecnologias as ver_tecnologias, eliminar_tecnologia
from sqlalchemy.orm import Session
from fastapi import HTTPException

def crear_tecnologia(tecnologia: TecnologiaCreate, db: Session):
    datos_tecnologias = tecnologia.model_dump()
    nueva_tecnologia = Tecnologia(**datos_tecnologias)
    return guardar_tecnologia(db, nueva_tecnologia)

def obtener_tecnologias(db: Session):
    tecnologias = ver_tecnologias(db)
    return tecnologias

def obtener_tecnologia_por_id(id: int, db: Session):
    tecnologia = ver_tecnologia_por_id(db, id)
    if not tecnologia:
        raise HTTPException(status_code=404, detail="La tecnologia no existe")
    return tecnologia

def modificar_tecnologia(id: int,db: Session,tecnologia_db: TecnologiaUpdate):
    tecnologia = ver_tecnologia_por_id(db, id)
    if not tecnologia:
        raise HTTPException(status_code=404, detail="La tecnologia no existe")
    datos_nuevos = tecnologia_db.model_dump(exclude_unset=True)
    datos_atualizados = atualizar_tecnologia(db,id,datos_nuevos)
    return datos_atualizados

def remover_tecnologia(id: int,db: Session):
    tecnologia = ver_tecnologia_por_id(db, id)
    if not tecnologia:
        raise HTTPException(status_code=404, detail="La tecnologia no existe")
    eliminar_tecnologia(db, id)
    return {"mensaje": "tecnologia eliminada con exito"}