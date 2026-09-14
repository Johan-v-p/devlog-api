from pwdlib import PasswordHash
import jwt
from datetime import datetime, timedelta, timezone
from app.core.config import settings

password_hash = PasswordHash.recommended()

def hashear_password(password: str) -> str:
    return password_hash.hash(password)
    

def verificar_password(password: str, hash_generado: str) -> bool:
    return password_hash.verify(password, hash_generado)

def crear_token(data: dict):

    expiracion = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)

    data.update({
        "exp": expiracion
    })

    data = jwt.encode(
        data,
        settings.secret_key,
        algorithm=settings.algorithm
        
    )

    return data

def verificar_token(token: str):
    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm]
        )

        return payload

    except jwt.InvalidTokenError:
        return None
