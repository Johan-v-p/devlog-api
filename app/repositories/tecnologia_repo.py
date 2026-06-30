from app.models.tecnologia import Tecnologia

def obtener_tecnologias(db):
    return db.query(Tecnologia).all()

def obtener_tecnologia_por_id(db, id: int):
    return db.query(Tecnologia).filter(Tecnologia.id == id).first()

def crear_tecnologia(db, tecnologia: Tecnologia):
    db.add(tecnologia)
    db.commit()
    db.refresh(tecnologia)
    return tecnologia

def atualizar_tecnologia(db, id:int, nuevos_datos: dict):
    tecnologia = db.query(Tecnologia).filter(Tecnologia.id == id).first()
    if not tecnologia:
        return False
    for campo, valor in nuevos_datos.items():
        setattr(tecnologia,campo,valor)
    db.commit()
    db.refresh(tecnologia)
    return tecnologia

def eliminar_tecnologia(db, id: int):
    tecnologia = db.query(Tecnologia).filter(Tecnologia.id == id).first()
    db.delete(tecnologia)
    db.commit()
    return True

