# Importando instâncias para rodar flask
from flask_openapi3 import OpenAPI, Tag
from flask import redirect

# Importando a instância do app criada em app.py
from app import app

# definindo tag para a rota de documentação
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")

# Rota da Documentação
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')
