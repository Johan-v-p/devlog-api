from app.models.sesion_tecnologia import SesionTecnologia

def obtener_sesion_tecnologias(db):
    return db.query(SesionTecnologia).all()

def obtener_sesion_tecnologia_por_id(db, id: int):
    return db.query(SesionTecnologia).filter(SesionTecnologia.id == id).first()

def crear_sesion_tecnologia(db, sesion_tecnologia: SesionTecnologia):
    db.add(sesion_tecnologia)
    db.commit()
    db.refresh(sesion_tecnologia)
    return sesion_tecnologia

def atualizar_sesion_tecnologia(db, id:int, nuevos_datos: dict):
    sesion_tecnologia = db.query(SesionTecnologia).filter(SesionTecnologia.id == id).first()
    if not sesion_tecnologia:
        return False
    for campo, valor in nuevos_datos.items():
        setattr(sesion_tecnologia,campo,valor)
    db.commit()
    db.refresh(sesion_tecnologia)
    return sesion_tecnologia

def eliminar_sesion_tecnologia(db, id: int):
    sesion_tecnologia = db.query(SesionTecnologia).filter(SesionTecnologia.id == id).first()
    db.delete(sesion_tecnologia)
    db.commit()
    return True

