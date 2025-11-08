from ..config.base import Base
from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Nota(Base):
    __tablename__ = "notas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nota = Column(Float, nullable=False)
    aluno_id = Column(Integer, nullable=False)
    atividade_id = Column(Integer, ForeignKey("atividade.id"))

    atividade = relationship("Atividade", back_populates="notas")

    def to_dict(self):
        return {
            "id": self.id,
            "nota": self.nota,
            "aluno_id": self.aluno_id,
            "atividade_id": self.atividade_id
               }