"""
Documentação das rotas de atividades.
"""

list_atividades = {
    "summary": "Lista todas as atividades",
    "tags": ["Atividades"],
    "responses": {
        "200": {
            "description": "Lista de atividades",
            "schema": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer",
                            "description": "ID da Atividade"
                        },
                        "nome_atividade": {
                            "type": "string",
                            "description": "Nome da Atividade"
                        },
                        "descricao": {
                            "type": "string",
                            "description": "descricao da Atividade"
                        },
                        "peso_porcento": {
                            "type": "float",
                            "description": "Peso em porcento da Atividade"
                        },
                        "data_entrega": {
                            "type": "string",
                            "format": "date",
                            "description": "Data de entrega da Atividade"
                        },
                        "turma_id": {
                            "type": "integer",
                            "description": "ID da Turma"
                        },
                        "professor_id": {
                            "type": "integer",
                            "description": "ID do Professor"
                        }
                    }
                }
            }
        },
            "204": {
            "description": "Nenhuma atividade encontrada"
        }
    }
}

get_atividade = {
    "summary": "Obtém uma atividade por ID",
    "tags": ["Atividades"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID da atividade"
        }
    ],
    "responses": {
        "200": {
            "description": "Detalhes da atividade",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "Atividade encontrada"
                    },
                    "data": {
                        "type": "object",
                        "properties": {
                            "reserva": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "integer",
                                        "description": "ID da Atividade"
                                    },
                                    "nome_atividade": {
                                        "type": "string",
                                        "description": "Nome da Atividade"
                                    },
                                    "descricao": {
                                        "type": "string",
                                        "description": "descricao da Atividade"
                                    },
                                    "peso_porcento": {
                                        "type": "float",
                                        "description": "Peso em porcento da Atividade"
                                    },
                                    "data_entrega": {
                                        "type": "string",
                                        "format": "date",
                                        "description": "Data de entrega da Atividade"
                                    },
                                    "turma_id": {
                                        "type": "integer",
                                        "description": "ID da Turma"
                                    },
                                    "professor_id": {
                                        "type": "integer",
                                        "description": "ID do Professor"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "404": {
            "description": "Atividade não encontrada"
        }
    }
}

create_atividade = {
    "summary": "Cria uma nova atividade",
    "tags": ["Atividades"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "nome_atividade": {
                        "type": "string",
                        "description": "Nome da Atividade"
                    },
                    "descricao": {
                        "type": "string",
                        "description": "descricao da Atividade"
                    },
                    "peso_porcento": {
                        "type": "Integer",
                        "description": "Peso em porcento da Atividade"
                    },
                    "data_entrega": {
                        "type": "string",
                        "format": "date",
                        "description": "Data de entrega da Atividade"
                    },
                    "turma_id": {
                        "type": "integer",
                        "description": "ID da turma que será vinculada à atividade"
                    },
                   "professor_id": {
                        "type": "integer",
                        "description": "ID do professor que será vinculada à atividade"
                    }
                },
                "required": ["nome_atividade", "turma_id", "professor_id"]
            }
        }
    ],
    "responses": {
        "201": {
            "description": "Atividade criada com sucesso",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "Atividade criada com sucesso"
                    },
                    "data": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "integer",
                                "description": "ID da atividade criado"
                            }
                        }
                    }
                }
            }
        },
        "400": {
            "description": "Erro ao criar atividade",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "description": "Mensagem de erro"
                    }
                }
            }
        }
    }
}

update_atividade = {
    "summary": "Atualiza uma atividade existente",
    "tags": ["Atividades"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID da atividade"
        },
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "nome_atividade": {
                        "type": "string",
                        "description": "Nome da Atividade"
                    },
                    "descricao": {
                        "type": "string",
                        "description": "descricao da Atividade"
                    },
                    "peso_porcento": {
                        "type": "float",
                        "description": "Peso em porcento da Atividade"
                    },
                    "data_entrega": {
                        "type": "string",
                        "format": "date",
                        "description": "Data de entrega da Atividade"
                    },
                    "turma_id": {
                        "type": "integer",
                        "description": "ID da turma que será vinculada à atividade"
                    },
                   "professor_id": {
                        "type": "integer",
                        "description": "ID do professor que será vinculada à atividade"
                    }
                }
            }
        }
    ],
    "responses": {
        "200": {
            "description": "Atividade atualizada com sucesso",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "Atividade atualizada com sucesso"
                    },
                    "data": {
                        "type": "object",
                        "properties": {
                            "reserva": {
                                "type": "object",
                                "properties": {
                                    "id": { "type": "integer" },
                                    "nome_atividade": { "type": "string" },
                                    "descricao": { "type": "string" },
                                    "peso_porcento": { "type": "float" },
                                    "data_entrega": { "type": "string", "format": "date" },
                                    "turma_id": { "type": "integer" },
                                    "professor_id": { "type": "integer"}
                            }
                        }
                    }
                }
            }
        },
        "400": { "description": "Dados inválidos ou conflito" },
        "404": { "description": "Atividade, professor ou turma não encontrado" },
        "500": { "description": "Erro interno" }
    }
}}

delete_atividade = {
    "summary": "Deleta uma atividade por ID",
    "tags": ["Atividades"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID da atividade"
        }
    ],
    "responses": {
        "200": {
            "description": "Atividade deletada com sucesso",
            "schema": {
                "type": "object",
                "properties": {
                    "message": { "type": "string", "example": "Atividade deletada com sucesso" }
                }
            }
        },
        "404": { "description": "Atividade não encontrada" },
        "500": { "description": "Erro interno" }
    }
}