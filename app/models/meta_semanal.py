from sqlalchemy import String, ForeignKey, Float, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base
from datetime import date

class MetasSemanal(Base):
    __tablename__ = "metas_semanales"
    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    titulo: Mapped[str] = mapped_column(String(150), nullable=False)
    descripcion: Mapped[str | None] = mapped_column()
    objetivo_horas: Mapped[float] = mapped_column(Float, nullable=False)
    fecha_inicio: Mapped[date] = mapped_column(nullable=False)
    fecha_fin: Mapped[date] = mapped_column(nullable=False)
    completada: Mapped[bool] = mapped_column(Boolean, default=False)