from app.models.meta_semanal import MetasSemanal

def obtener_metas_semanal(db):
    return db.query(MetasSemanal).all()

def obtener_meta_semanal_por_id(db, id: int):
    return db.query(MetasSemanal).filter(MetasSemanal.id == id).first()

def crear_meta_semanal(db, meta_semanal: MetasSemanal):
    db.add(meta_semanal)
    db.commit()
    db.refresh(meta_semanal)
    return meta_semanal

def atualizar_meta_semanal(db, id:int, nuevos_datos: dict):
    meta_semanl = db.query(MetasSemanal).filter(MetasSemanal.id == id).first()
    if not meta_semanl:
        return False
    for campo, valor in nuevos_datos.items():
        setattr(meta_semanl,campo,valor)
    db.commit()
    db.refresh(meta_semanl)
    return meta_semanl

def eliminar_meta_semanal(db, id: int):
    meta_semanal = db.query(MetasSemanal).filter(MetasSemanal.id == id).first()
    db.delete(meta_semanal)
    db.commit()
    return True

