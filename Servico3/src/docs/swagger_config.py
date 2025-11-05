from flasgger import Swagger

template = {
    "swagger": "2.0",
    "info": {
        "title": "API Atividades e Notas",
        "description": "API para gerenciamento de atividades e notas dos alunos",
        "version": "1.0.0"
    },
    "tags": [
        {
            "name": "Atividades",
            "description": "Operações relacionadas a Atividades dos alunos"
        },
        {
            "name": "Notas",
            "description": "Operações relacionadas a Notas dos alunos"
        }
    ]
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec",
            "route": "/apispec.json",
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/"
}

def setup_swagger(app):
    swagger = Swagger(
        app,
        template=template,
        config=swagger_config
    )
    return swagger