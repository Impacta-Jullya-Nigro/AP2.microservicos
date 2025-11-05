from flask import Flask
from src.config.base import Base, engine
from src.controllers.atividade_controller import atividade_bp
from src.controllers.nota_controller import nota_bp
from src.docs.swagger_config import setup_swagger

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco_servico3.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    Base.metadata.create_all(bind=engine)
    
    setup_swagger(app)

    app.register_blueprint(atividade_bp, url_prefix="/atividades")
    app.register_blueprint(nota_bp, url_prefix="/notas")
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host= '0.0.0.0', port=5002, debug=True)