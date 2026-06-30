# app/core/database.py
# SQLAlchemy necesita tres piezas para conectarse a la base de datos:
# 1. Engine    → la conexión física a PostgreSQL
# 2. Session   → cada "conversación" con la base de datos
# 3. Base      → la clase padre de todos nuestros modelos

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from app.core.config import settings

# El engine es la conexión real a PostgreSQL
# usa la URL que definiste en el .env
engine = create_engine(settings.database_url)

# SessionLocal es la fábrica de sesiones
# cada request HTTP abre una sesión y la cierra al terminar
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,  # los cambios no se guardan solos — tú decides cuándo
    autoflush=False    # no envía queries a la BD hasta que tú lo indiques
)

# Base es la clase padre de todos los modelos
# cuando hagas "class Sesion(Base)" SQLAlchemy sabe que es una tabla
class Base(DeclarativeBase):
    pass

# Función generadora — abre una sesión por request y la cierra al terminar
# el "yield" es clave: garantiza que la sesión se cierra aunque haya un error
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
