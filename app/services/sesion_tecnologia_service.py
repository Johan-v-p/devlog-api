from app.schemas.sesion_tecnologia import SesionTecnologiaCreate, SesionTecnologiaUpdate
from app.models.sesion_tecnologia import SesionTecnologia
from app.repositories.sesion_tecnologia_repo import crear_sesion_tecnologia as guardar_sesion_tecnologia, atualizar_sesion_tecnologia, obtener_sesion_tecnologia_por_id as ver_sesion_tecnologia_por_id, obtener_sesion_tecnologias as ver_sesion_tecnologias, eliminar_sesion_tecnologia
from sqlalchemy.orm import Session
from fastapi import HTTPException

def crear_sesion_tecnologia(sesion_tecnologia: SesionTecnologiaCreate, db: Session):
    datos_sesion_tecnologias = sesion_tecnologia.model_dump()
    nueva_sesion_tecnologia = SesionTecnologia(**datos_sesion_tecnologias)
    return guardar_sesion_tecnologia(db, nueva_sesion_tecnologia)

def obtener_sesion_tecnologias(db: Session):
    sesion_tecnologias = ver_sesion_tecnologias(db)
    return sesion_tecnologias

def obtener_sesion_tecnologia_por_id(id: int, db: Session):
    sesion_tecnologia = ver_sesion_tecnologia_por_id(db, id)
    if not sesion_tecnologia:
        raise HTTPException(status_code=404, detail="La sesion tecnologia no existe")
    return sesion_tecnologia

def modificar_sesion_tecnologia(id: int,db: Session,sesion_tecnologia_db: SesionTecnologiaUpdate):
    sesion_tecnologia = ver_sesion_tecnologia_por_id(db, id)
    if not sesion_tecnologia:
        raise HTTPException(status_code=404, detail="La sesion tecnologia no existe")
    datos_nuevos = sesion_tecnologia_db.model_dump(exclude_unset=True)
    datos_atualizados = atualizar_sesion_tecnologia(db,id,datos_nuevos)
    return datos_atualizados

def remover_sesion_tecnologia(id: int,db: Session):
    sesion_tecnologia = ver_sesion_tecnologia_por_id(db, id)
    if not sesion_tecnologia:
        raise HTTPException(status_code=404, detail="La sesion tecnologia no existe")
    eliminar_sesion_tecnologia(db, id)
    return {"mensaje": "sesion tecnologia eliminada con exito"}