from fastapi import APIRouter

router = APIRouter(prefix="/metas_semanalales", tags=["metas_semanales"])

@router.get("/")
def obtener_metas_semanal():
    return None

@router.get("/{id}")
def obtener_meta_semanal(id: int):
    return None

@router.post("/")
def crear_meta_semanal():
    return None

@router.put("/{id}")
def atualizar_meta_semanal(id: int):
    return None
