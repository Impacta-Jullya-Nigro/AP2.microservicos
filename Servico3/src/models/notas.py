from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import relationship
from ..config.base import Base


class Nota(Base):
    __tablename__ = "notas"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nota = Column(Float, nullable=False)
    aluno_id = Column(Integer, nullable=False)
    atividade_id = Column(Integer, nullable=False)

    aluno = relationship("Alunos", back_populates="notas")
    atividade = relationship("Atividades", back_populates="notas")

def to_dict(self):
        return {
            "id": self.id,
            "nota ": self.nota.isoformat() if self.nota else None,
            "aluno_id": self.aluno_id,
            "atividade_id": self.atividade_id}