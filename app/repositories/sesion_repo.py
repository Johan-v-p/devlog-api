from app.models.sesion import Sesion

def obtener_sesiones(db):
    return db.query(Sesion).all()

def obtener_sesion_por_id(db, id: int):
    return db.query(Sesion).filter(Sesion.id == id).first()

def crear_sesion(db, sesion: Sesion):
    db.add(sesion)
    db.commit()
    db.refresh(sesion)
    return sesion

def atualizar_sesion(db, id: int, nuevos_datos: dict):
    sesion = db.query(Sesion).filter(Sesion.id == id).first()
    if not sesion:
        return False
    for campo,valor in nuevos_datos.items():
        setattr(sesion, campo, valor)
    db.commit()
    db.refresh(sesion)
    return sesion


def eliminar_sesion(db, id: int):
    sesion = db.query(Sesion).filter(Sesion.id == id).first()
    db.delete(sesion)
    db.commit()
    return True