from fastapi import APIRouter

router = APIRouter(prefix="/tecnologias", tags=["tecnologias"])

@router.get("/")
def obtener_tecnologias():
    return None

@router.get("/{id}")
def obtener_tecnologia(id: int):
    return None

@router.post("/")
def crear_tecnologia():
    return None

@router.put("/{id}")
def atualizar_tecnologia(id: int):
    return None
