from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.usuario import UsuarioCreate, UsuarioResponse, UsuarioUpdate
from app.services.usuario_service import crear_usuario as crear_usuario_service, obtener_usuarios as obtener_usuarios_service, obtener_usuario_por_id as obtener_usuario_por_id_service, modificar_usuario, remover_usuario
from app.core.database import get_db


router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.get("/", response_model=list[UsuarioResponse])
def obtener_usuarios(db: Session = Depends(get_db)):
    return obtener_usuarios_service(db)

@router.get("/{id}", response_model=UsuarioResponse)
def obtener_usuario_por_id(id: int, db: Session = Depends(get_db)):
    return obtener_usuario_por_id_service(id, db)

@router.post("/", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return crear_usuario_service(usuario, db)

@router.put("/{id}", response_model=UsuarioResponse)
def atualizar_usuario(id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    return modificar_usuario(id, db, usuario)

@router.delete("/{id}")
def eliminar_usuario(id: int, db: Session = Depends(get_db)):
    return remover_usuario(id, db)


