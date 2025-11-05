"""
Documentação das rotas de notas.
"""

list_notas = {
    "summary": "Lista todas as notas",
    "tags": ["Notas"],
    "responses": {
        "200": {
            "description": "Lista de notas encontradas",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "Notas encontradas"
                    },
                    "data": {
                        "type": "object",
                        "properties": {
                            "reservas": {
                                "type": "array",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer",
                                            "description": "ID da nota"
                                        },
                                        "nota": {
                                            "type": "number",
                                            "format": "float",
                                            "description": "Nota atribuída"
                                        },
                                        "aluno_id": {
                                            "type": "integer",
                                            "description": "ID do aluno"
                                        },
                                        "atividade_id": {
                                            "type": "integer",
                                            "description": "ID da atividade"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "204": {
            "description": "Nenhuma nota encontrada"
        }
    }
}

get_nota = {
    "summary": "Obtém uma nota por ID",
    "tags": ["Notas"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID da nota"
        }
    ],
    "responses": {
        "200": {
            "description": "Detalhes da nota",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "Nota encontrada"
                    },
                    "data": {
                        "type": "object",
                        "properties": {
                            "reserva": {
                                "type": "object",
                                "properties": {
                                        "id": {
                                            "type": "integer",
                                            "description": "ID da nota"
                                        },
                                        "nota": {
                                            "type": "number",
                                            "format": "float",
                                            "description": "Nota atribuída"
                                        },
                                        "aluno_id": {
                                            "type": "integer",
                                            "description": "ID do aluno"
                                        },
                                        "atividade_id": {
                                            "type": "integer",
                                            "description": "ID da atividade"
                                        }
                                }
                            }
                        }
                    }
                }
            }
        },
        "404": {
            "description": "Nota não encontrada"
        }
    }
}

create_nota = {
    "summary": "Cria uma nova nota",
    "tags": ["Notas"],
    "parameters": [
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "ID da nota"
                    },
                     "nota": {
                        "type": "number",
                        "format": "float",
                        "description": "Nota atribuída"
                    },
                    "aluno_id": {
                        "type": "integer",
                        "description": "ID do aluno que será vinculada à nota"
                    },
                    "atividade_id": {
                        "type": "integer",
                        "description": "ID da atividade que será vinculada à nota"
                    }
                },
                "required": ["nota", "aluno_id", "atividade_id"]
            }
        }
    ],
    "responses": {
        "201": {
            "description": "Nota criada com sucesso",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "Nota criada com sucesso"
                    },
                    "data": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "integer",
                                "description": "ID da Nota criada"
                            }
                        }
                    }
                }
            }
        },
        "400": {
            "description": "Erro ao criar nota",
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

update_nota = {
    "summary": "Atualiza uma nota existente",
    "tags": ["Notas"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID da nota a ser atualizada"
        },
        {
            "name": "body",
            "in": "body",
            "required": True,
            "schema": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "ID da nota"
                    },
                     "nota": {
                        "type": "number",
                        "format": "float",
                        "description": "Nota atribuída"
                    },
                    "aluno_id": {
                        "type": "integer",
                        "description": "ID do aluno que será vinculada à nota"
                    },
                    "atividade_id": {
                        "type": "integer",
                        "description": "ID da atividade que será vinculada à nota"
                    }
                }
            }
        }
    ],
    "responses": {
        "200": {
            "description": "Nota atualizada com sucesso",
            "schema": {
                "type": "object",
                "properties": {
                    "message": {
                        "type": "string",
                        "example": "Nota atualizada com sucesso"
                    },
                    "data": {
                        "type": "object",
                        "properties": {
                            "reserva": {
                                "type": "object",
                                "properties": {
                                    "id": { "type": "integer" },
                                    "nota": { "type": "number", "format": "float" },
                                    "aluno_id": { "type": "integer" },
                                    "atividade_id": { "type": "integer"}
                            }
                        }
                    }
                }
            }
        },
        "400": { "description": "Dados inválidos ou conflito" },
        "404": { "description": "Nota, aluno ou atividade não encontrada" },
        "500": { "description": "Erro interno" }
    }
}
}

delete_nota = {
    "summary": "Deleta uma nota por ID",
    "tags": ["Notas"],
    "parameters": [
        {
            "name": "id",
            "in": "path",
            "type": "integer",
            "required": True,
            "description": "ID da nota a ser deletada"
        }
    ],
    "responses": {
        "200": {
            "description": "Nota deletada com sucesso",
            "schema": {
                "type": "object",
                "properties": {
                    "message": { "type": "string", "example": "Nota deletada com sucesso" }
                }
            }
        },
        "404": { "description": "Nota não encontrada" },
        "500": { "description": "Erro interno" }
    }
}