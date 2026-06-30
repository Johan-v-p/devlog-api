# app/core/config.py
# pydantic-settings lee automáticamente el archivo .env
# y valida que las variables tengan el tipo correcto

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Datos de la aplicación
    app_name: str
    app_version: str
    debug: bool

    # Base de datos
    database_url: str

    class Config:
        # Le dice a pydantic dónde encontrar el archivo .env
        env_file = ".env"

# Instancia única que se importa en todo el proyecto
# En lugar de leer el .env en cada archivo, lo lees una vez aquí
settings = Settings()
