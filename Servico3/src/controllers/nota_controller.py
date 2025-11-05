from flask import Flask, jsonify, request, Blueprint
from sqlalchemy.orm import Session
from src.config.base import SessionLocal
from src.models.notas import Nota
from src.docs.nota_docs import list_notas, get_nota, create_nota, update_nota, delete_nota
from flasgger import swag_from

nota_bp = Blueprint("nota", __name__)

@nota_bp.route("/", methods=["GET"])
@swag_from(list_notas)
def get_notas():
    session = SessionLocal()
    try:
        notas = session.query(Nota).all()

        if len(notas) == 0 or notas is None:
            return jsonify({"message": "Nenhuma nota encontrada"}), 204
        
        return jsonify({"message": "Notas encontradas", "data": [n.to_dict() for n in notas]}), 200
    finally:
        session.close()


@nota_bp.route("/", methods=["GET"])
@swag_from(get_nota)
def get_nota(id):
    session = SessionLocal()
    try:
        nota = session.query(Nota).filter(Nota.id == id).first()

        if nota is None:
            return jsonify({"message": "Nenhuma nota encontrada"}), 204
        
        aluno = nota.aluno_id
        atividade = nota.atividade_id

        if not aluno:
            return jsonify({"message": "Aluno não encontrado no Serviço 1"}), 404
        
        if not atividade:
            return jsonify({"message": "Atividade não encontrada no Serviço 3"}), 404
        
        nota.aluno = aluno
        nota.atividade = atividade
        
        return jsonify({"message": "Notas encontradas"}), 200
    finally:
        session.close()

@nota_bp.route("/<int:id>", methods=["POST"])
@swag_from(create_nota)
def create_nota():
    session = SessionLocal()
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message": "Dados da nota não fornecidos"}), 400

        required_fields = ['aluno_id', 'atividade_id', 'nota']
        for field in required_fields:
            if field not in data:
                return jsonify({"message": f"Campo {field} é obrigatório"}), 400

        nova_nota = Nota(
            aluno_id=data['aluno_id'],
            atividade_id=data['atividade_id'],
            valor_nota=data['nota']
        )

        session.add(nova_nota)
        session.commit()

        return jsonify({"message": "Nota criada com sucesso"}), 201
    finally:
        session.close()

@nota_bp.route("/<int:id>", methods=["PUT"])
@swag_from(update_nota)
def update_nota(id):
    session = SessionLocal()
    try:
        nota = session.query(Nota).filter(Nota.id == id).first()

        if nota is None:
            return jsonify({"message": "Nota não encontrada"}), 404

        data = request.get_json()
        if not data:
            return jsonify({"message": "Dados da nota não fornecidos"}), 400

        if 'aluno_id' in data:
            nota.aluno_id = data['aluno_id']

        if 'atividade_id' in data:
            nota.atividade_id = data['atividade_id']

        if 'nota' in data:
            nota.valor_nota = data['nota']

        session.commit()

        return jsonify({"message": "Nota atualizada com sucesso"}), 200
    finally:
        session.close()

@nota_bp.route("/<int:id>", methods=["DELETE"])
@swag_from(delete_nota)
def delete_nota(id):
    session = SessionLocal()
    try:
        nota = session.query(Nota).filter(Nota.id == id).first()

        if nota is None:
            return jsonify({"message": "Nota não encontrada"}), 404

        session.delete(nota)
        session.commit()

        return jsonify({"message": "Nota deletada com sucesso"}), 200
    finally:
        session.close()
