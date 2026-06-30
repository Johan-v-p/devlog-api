from fastapi import APIRouter

router = APIRouter(prefix="/sesion_tecnologias", tags=["sesion_tecnologias"])

@router.get("/")
def obtener_sesion_tecnologias():
    return None

@router.get("/{id}")
def obtener_sesion_tecnologia(id: int):
    return None

@router.post("/")
def crear_sesion_tecnologia():
    return None

@router.put("/{id}")
def atualizar_sesion_tecnologia(id: int):
    return None
