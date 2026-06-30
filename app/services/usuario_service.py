from app.schemas.usuario import UsuarioCreate, UsuarioUpdate
from app.models.usuario import Usuario
from app.repositories.usuario_repo import obtener_usuarios as ver_usuarios, obtener_usuario_por_id as ver_usuario_por_id, obtener_usuario_por_email, crear_usuario as guardar_usuario, atualizar_usuario , eliminar_usuario
from app.core.security import hashear_password
from sqlalchemy.orm import Session
from fastapi import HTTPException

def crear_usuario(usuario: UsuarioCreate, db: Session):
    email_normalizado = usuario.email.strip().lower()
    usuario_existente = obtener_usuario_por_email(db, email_normalizado)
    if usuario_existente:
        raise HTTPException(status_code=409, detail="Error el usuario ya existe")
    datos_usuarios = usuario.model_dump()
    datos_usuarios["password_hash"] = hashear_password(usuario.password)
    del datos_usuarios["password"]
    datos_usuarios["email"] = email_normalizado
    nuevo_usuario = Usuario(**datos_usuarios)
    return guardar_usuario(db, nuevo_usuario)

def obtener_usuarios(db: Session):
    usuarios = ver_usuarios(db)
    return usuarios

def obtener_usuario_por_id(id: int, db: Session):
    usuario = ver_usuario_por_id(db,id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Error el usuario no existe")
    
    return usuario
    
def modificar_usuario(id: int, db: Session, usuario_db: UsuarioUpdate):
    usuario = ver_usuario_por_id(db,id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Error el usuario no existe")
    
    datos_nuevos = usuario_db.model_dump(exclude_unset=True)

    if "password" in datos_nuevos:
        hash = hashear_password(datos_nuevos["password"])
        datos_nuevos["password_hash"] = hash
        del datos_nuevos["password"]
    
    datos_atualizados = atualizar_usuario(db,id, datos_nuevos)
    return datos_atualizados

def remover_usuario(id: int, db: Session):
    usuario = ver_usuario_por_id(db,id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Error el usuario no existe")
    
    eliminar_usuario(db, id)
    return {"mensaje": "usuario eliminado con exito"}