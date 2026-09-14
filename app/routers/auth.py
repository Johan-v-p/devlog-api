from fastapi import APIRouter ,Depends
from app.schemas.auth import TokenCreate, TokenResponse
from sqlalchemy.orm import Session
from app.repositories.usuario_repo import obtener_usuario_por_email
from app.core.security import verificar_password, crear_token
from app.core.database import get_db
from fastapi import HTTPException

router = APIRouter()

@router.post("/auth/login", response_model=TokenResponse)
def login(token: TokenCreate, db: Session = Depends(get_db)):
    usuario = obtener_usuario_por_email(db, token.email)
    if not usuario:
        raise HTTPException(status_code=401, detail="email o contraseña incorrecto")
    contraseña = verificar_password(token.password, usuario.password_hash)
    if not contraseña:
        raise HTTPException(status_code=401, detail="contraseña incorrecta")

    return TokenResponse(token=crear_token({"sub": str(usuario.id)}))