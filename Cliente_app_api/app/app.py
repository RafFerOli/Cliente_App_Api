from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS

info = Info(title="API - Cadastro de Empresas", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Importando as rotas
import routes.rts_schemas
import routes.rts_cliente