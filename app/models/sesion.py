from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from datetime import date

class Sesion(Base):
    __tablename__ = "sesiones"
    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    fecha: Mapped[date] = mapped_column()
    horas_totales: Mapped[float] = mapped_column(Float, nullable=False)
    nivel_energia: Mapped[int] = mapped_column(nullable=False)
    notas: Mapped[str | None] = mapped_column()