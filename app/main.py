from fastapi import FastAPI
from app.routers.metas_semanales import router as metas_semanales_router
from app.routers.sesion_tecnologias import router as sesion_tecnologias_router
from app.routers.sesiones import router as sesiones_router
from app.routers.tecnologias import router as tecnologias_router
from app.routers.usuarios import router as usuarios_router
from app.routers.auth import router as auth_router

app = FastAPI()

app.include_router(metas_semanales_router)
app.include_router(sesion_tecnologias_router)
app.include_router(sesiones_router)
app.include_router(tecnologias_router)
app.include_router(usuarios_router)
app.include_router(auth_router)