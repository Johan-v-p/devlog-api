from fastapi import APIRouter

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.get("/")
def obtener_usuarios():
    return None

@router.get("/{id}")
def obtener_usuario(id: int):
    return None

@router.post("/")
def crear_usuario():
    return None

@router.put("/{id}")
def atualizar_usuario(id: int):
    return None
