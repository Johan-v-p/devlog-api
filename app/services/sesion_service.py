from app.schemas.sesion import SesionCreate, SesionUpdate
from app.models.sesion import Sesion
from app.repositories.sesion_repo import crear_sesion as guardar_sesion, atualizar_sesion, obtener_sesion_por_id as ver_sesion_por_id, obtener_sesiones as ver_sesiones, eliminar_sesion
from sqlalchemy.orm import Session
from fastapi import HTTPException

  
def crear_sesion(sesion: SesionCreate,usuario_id: int, db:Session):
    datos_sesion = sesion.model_dump()
    datos_sesion["usuario_id"] = usuario_id
    nueva_sesion = Sesion(**datos_sesion)
    return guardar_sesion(db, nueva_sesion)

def obtener_sesiones(db: Session):
    sesiones = ver_sesiones(db)
    return sesiones

def obtener_sesion_por_id(id: int, db: Session):
    sesion = ver_sesion_por_id(db, id)
    if not sesion:
        raise HTTPException(status_code=404, detail="La sesion no existe")
    return sesion

def modificar_sesion(id: int,db: Session,sesion_db: SesionUpdate):
    sesion = ver_sesion_por_id(db, id)
    if not sesion:
        raise HTTPException(status_code=404, detail="La sesion no existe")
    datos_nuevos = sesion_db.model_dump(exclude_unset=True)
    datos_atualizados = atualizar_sesion(db,id,datos_nuevos)
    return datos_atualizados

def remover_sesion(id: int,db: Session):
    sesion = ver_sesion_por_id(db, id)
    if not sesion:
        raise HTTPException(status_code=404, detail="La sesion no existe")
    eliminar_sesion(db, id)
    return {"mensaje": "sesion eliminada con exito"}