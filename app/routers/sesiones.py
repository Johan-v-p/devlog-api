from fastapi import APIRouter

router = APIRouter(prefix="/sesiones", tags=["sesiones"])

@router.get("/")
def obtener_sesiones():
    return None

@router.get("/{id}")
def obtener_sesion(id: int):
    return None

@router.post("/")
def crear_sesion():
    return None

@router.put("/{id}")
def atualizar_sesion(id: int):
    return None
