from flask import Flask, Blueprint, request, jsonify
from sqlalchemy.orm import Session
from src.config.base import SessionLocal
from src.models.atividades import Atividade
from src.services.professor_service import ProfessorService
from src.services.turma_service import TurmaService
from flasgger import swag_from
from src.docs.atividade_docs import list_atividades, get_atividade, create_atividade, update_atividade, delete_atividade

atividade_bp = Blueprint("atividade", __name__)

@atividade_bp.route("/", methods=["GET"])
@swag_from(list_atividades)
def get_atividades():
    session = SessionLocal()
    try:
        atividade = session.query(Atividade).all()

        if len(atividade) == 0 or atividade is None:
            return jsonify({"message": "Nenhuma atividade encontrada"}), 204
        
        return jsonify({"message": "Atividades encontradas", "data": [a.to_dict() for a in atividade]}), 200
    finally:
        session.close()

@atividade_bp.route("/<int:id>", methods=["GET"])
@swag_from(get_atividade)
def get_atividade(id):
    session = SessionLocal()
    try:
        atividade = session.query(Atividade).filter(Atividade.id == id).first()

        if atividade is None:
            return jsonify({"message": "Atividade não encontrada"}), 404

        turma = TurmaService.get_turma(atividade.turma_id)
        professor = ProfessorService.get_professor(atividade.professor_id)

        if not turma:
            return jsonify({"message": "Turma não encontrada no Serviço 1"}), 404
        
        if not professor:
            return jsonify({"message": "Professor não encontrado no Serviço 1"}), 404
        
        atividade.turma = turma
        atividade.professor = professor

        return jsonify({"message": "Atividade encontrada", "data": atividade.to_dict()}), 200
    finally:
        session.close()

@atividade_bp.route("/", methods=["POST"])
@swag_from(create_atividade)
def create_atividade():
    session = SessionLocal()
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message": "Dados da atividade não fornecidos"}), 400

        required_fields = ['turma_id', 'professor_id', 'nome_atividade']
        for field in required_fields:
            if field not in data:
                return jsonify({"message": f"Campo {field} é obrigatório"}), 400

        turma = TurmaService.get_turma(data['turma_id'])
        if not turma:
            return jsonify({"message": "Turma não encontrada no Serviço 1"}), 404

        professor = ProfessorService.get_professor(data['professor_id'])
        if not professor:
            return jsonify({"message": "Professor não encontrado no Serviço 1"}), 404

        nova_atividade = Atividade(
            turma_id=data['turma_id'],
            professor_id=data['professor_id'],
            nome_atividade=data['nome_atividade'],
            data_entrega=data['data_entrega']
        )

        session.add(nova_atividade)
        session.commit()

        return jsonify({"message": "Atividade criada com sucesso", "data": nova_atividade.to_dict()}), 201
    finally:
        session.close()

@atividade_bp.route("/<int:id>", methods=["PUT"])
@swag_from(update_atividade)
def update_atividade(id):
    session = SessionLocal()
    try:
        atividade = session.query(Atividade).filter(Atividade.id == id).first()

        if atividade is None:
            return jsonify({"message": "Atividade não encontrada"}), 404

        data = request.get_json()
        if 'turma_id' in data:
            turma = TurmaService.get_turma(data['turma_id'])
            if not turma:
                return jsonify({"message": "Turma não encontrada no Serviço 1"}), 404
            atividade.turma_id = data['turma_id']
        
        if 'professor_id' in data:
            professor = ProfessorService.get_professor(data['professor_id'])
            if not professor:
                return jsonify({"message": "Professor não encontrado no Serviço 1"}), 404
            atividade.professor_id = data['professor_id']
        
        if 'nome_atividade' in data:
            atividade.nome_atividade = data['nome_atividade']

        if 'data_entrega' in data:
            atividade.data_entrega = data['data_entrega']

        if 'descricao' in data:
            atividade.descricao = data['descricao']
            
        if 'peso_porcento' in data:
            atividade.peso_porcento = data['peso_porcento']

        session.commit()

        return jsonify({"message": "Atividade atualizada com sucesso", "data": atividade.to_dict()}), 200
    finally:
        session.close()

@atividade_bp.route("/<int:id>", methods=["DELETE"])
@swag_from(delete_atividade)
def delete_atividade(id):
    session = SessionLocal()
    try:
        atividade = session.query(Atividade).filter(Atividade.id == id).first()

        if atividade is None:
            return jsonify({"message": "Atividade não encontrada"}), 404

        session.delete(atividade)
        session.commit()

        return jsonify({"message": "Atividade deletada com sucesso"}), 200
    finally:
        session.close()
