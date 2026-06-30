from app.models.usuario import Usuario

def obtener_usuarios(db):
    return db.query(Usuario).all()

def obtener_usuario_por_id(db, id: int):
    return db.query(Usuario).filter(Usuario.id == id).first()

def crear_usuario(db, usuario: Usuario):
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario    

def atualizar_usuario(db, id: int, nuevos_datos: dict):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        return False
    for campo, valor in nuevos_datos.items():
            setattr(usuario, campo, valor)
    db.commit()
    db.refresh(usuario)
    return usuario
    

def eliminar_usuario(db, id: int):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    db.delete(usuario)
    db.commit()
    return True

def obtener_usuario_por_email(db, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()

