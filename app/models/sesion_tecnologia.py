from sqlalchemy import ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base

class SesionTecnologia(Base):
    __tablename__ = "sesion_tecnologias"
    id: Mapped[int] = mapped_column(primary_key=True)
    sesion_id: Mapped[int] = mapped_column(ForeignKey("sesiones.id"))
    tecnologia_id: Mapped[int] = mapped_column(ForeignKey("tecnologias.id"))
    horas: Mapped[float] = mapped_column(Float, nullable=False)