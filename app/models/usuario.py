from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from datetime import datetime

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100),nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String(150), unique= True, index= True, nullable=False)
    creado_en: Mapped[datetime] = mapped_column(server_default=func.now())

