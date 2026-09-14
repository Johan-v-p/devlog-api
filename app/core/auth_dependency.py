from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.core.security import verificar_token  

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def obtener_usuario_actual(token: str = Depends(oauth2_scheme)) -> int:
    """
    Dependencia para proteger endpoints. 
    Verifica el JWT y retorna el usuario_id (sub).
    """

    datos_token = verificar_token(token)
    
    if datos_token is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas o expiradas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    usuario_id: str = datos_token.get("sub")
    if usuario_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido: falta el identificador de usuario",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    return int(usuario_id)
