from sqlalchemy import Column, Date, Integer, String, Float
from ..config.base import Base
from sqlalchemy.orm import relationship


class Atividade(Base):
    __tablename__ = 'atividade'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_atividade = Column(String(100), nullable=False)
    descricao = Column(Integer, nullable=False)
    peso_porcento = Column(Integer, nullable=False)
    data_entrega = Column(Date, nullable=False)
    turma_id = Column(Integer, nullable=False) 
    professor_id = Column(Integer, nullable=False)

    atividades = []

    notas = relationship("Nota", back_populates="atividade", cascade="all, delete-orphan")
    atividade = relationship("Professor", back_populates="atividades", cascade="all, delete-orphan")
    
    def to_dict(self):
        return {
            "id": self.id,
            "nome_atividade ": self.nome_atividade ,
            "descricao": self.descricao,
            "peso_porcento": self.peso_porcento,
            "data_entrega": self.data_entrega.isoformat() if self.data_entrega else None,
            "turma_id": self.turma_id,
            "professor_id": self.professor_id,}