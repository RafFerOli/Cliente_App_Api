# Importando instâncias para rodar flask
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

# Importando instâncias para rodar sqlalchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func

# Importando instancias gerais
from urllib.parse import unquote
from model import Session, Cliente
from logger import logger
from schemas import *

# Importando a instância do app criada em app.py
from app import app

# definindo tag para as rotas de cliente
cliente_tag = Tag(name="Cliente", description="Adição, visualização e remoção de clientes na base")

#-------------------------------------------------------------------------------------
# Post: Cliente
#-------------------------------------------------------------------------------------
@app.post('/Cliente', tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_Cliente(form: ClienteSchema):
    """Adiciona um novo cliente à base de dados

    Retorna uma representação do cliente adicionado
    """
    cliente = Cliente(
        nome=form.nome,
        cnpj=form.cnpj,
        razao=form.razao,
        endereco=form.endereco,
        numero=form.numero,
        cidade=form.cidade,
        estado=form.estado,
        bairro=form.bairro,
        cep=form.cep,
        telefone=form.telefone,
        email=form.email
        )
    logger.debug(f"Adicionando cliente de nome: '{cliente.nome}'")
    try:
        # criando conexão com a base
        session = Session()
        # adicionando Cliente
        session.add(cliente)
        # efetivando o camando de adição de novo item na tabela
        session.commit()
        logger.debug(f"Adicionado cliente de nome: '{cliente.nome}'")
        return apresenta_cliente(cliente), 200

    except IntegrityError as e:
        # como a duplicidade do nome é a provável razão do IntegrityError
        error_msg = "Cliente de mesmo nome ou cnpj já salvo na base :/"
        logger.warning(f"Erro ao adicionar cliente '{cliente.nome}', {error_msg}")
        return {"mesage": error_msg}, 409

    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar cliente '{cliente.nome}', {error_msg}")
        return {"mesage": error_msg}, 400

#-------------------------------------------------------------------------------------
# Delete: Cliente
#-------------------------------------------------------------------------------------

@app.delete('/Cliente', tags=[cliente_tag],
            responses={"200": ClienteDelSchema, "404": ErrorSchema})
def del_Cliente(query: ClienteBuscaSchema):
    """Deleta um cliente a partir do nome de cliente informado

    Retorna uma mensagem de confirmação da remoção.
    """
    cliente_nome = unquote(unquote(query.nome))
    print(cliente_nome)
    logger.debug(f"Deletando dados sobre o cliente #{cliente_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Cliente).filter(func.lower(Cliente.nome) == cliente_nome.lower()).delete(synchronize_session='fetch')
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado Cliente #{cliente_nome}")
        return {"mesage": "Cliente removido", "id": cliente_nome}
    else:
        # se o Cliente não foi encontrado
        error_msg = "Cliente não encontrado na base :/"
        logger.warning(f"Erro ao deletar Cliente #'{cliente_nome}', {error_msg}")
        return {"mesage": error_msg}, 404

#-------------------------------------------------------------------------------------
# Put: Cliente
#-------------------------------------------------------------------------------------

@app.put('/Cliente', tags=[cliente_tag],
          responses={"200": ClienteViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def put_Cliente(form: ClienteSchema):
    """Modifica um cliente da base de dados

    Retorna uma mensagem de confirmação da modificação.
    """
    cliente_nome = unquote(unquote(form.nome))
    print(cliente_nome)
    logger.debug(f"Modificando dados sobre o cliente #{cliente_nome}")
    # criando conexão com a base
    session = Session()

    # selecinando linha que se deseja alterar
    count = session.query(Cliente).filter(func.lower(Cliente.nome) == cliente_nome.lower()).first()

    # Atualizando valores do registro
    count.numero = form.numero
    count.nome=form.nome
    count.cnpj=form.cnpj
    count.razao=form.razao
    count.endereco=form.endereco
    count.numero=form.numero
    count.cidade=form.cidade
    count.estado=form.estado
    count.bairro=form.bairro
    count.cep=form.cep
    count.telefone=form.telefone
    count.email=form.email

    # Confirme as alterações no banco de dados 
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Modificado Cliente #{cliente_nome}")
        return {"mesage": "Cliente modificado", "id": cliente_nome}
    else:
        # se o Cliente não foi encontrado
        error_msg = "Cliente não encontrado na base :/"
        logger.warning(f"Erro ao Modificar Cliente #'{cliente_nome}', {error_msg}")
        return {"mesage": error_msg}, 404

#-------------------------------------------------------------------------------------
# Get: Clientes
#-------------------------------------------------------------------------------------

@app.get('/Clientes', tags=[cliente_tag],
         responses={"200": ListagemClientesSchema, "404": ErrorSchema})
def get_Clientes():
    """Faz a busca por todos os clientes cadastrados

    Retorna uma representação da listagem de clientes.
    """
    logger.debug(f"Coletando clientes ")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    clientes = session.query(Cliente).all()

    if not clientes:
        # se não há Clientes cadastrados
        return {"Clientes": []}, 200
    else:
        logger.debug(f"%d rodutos econtrados" % len(clientes))
        # retorna a representação de Cliente
        print(clientes)
        return apresenta_clientes(clientes), 200

#-------------------------------------------------------------------------------------
# Get: Cliente (query: nome)
#-------------------------------------------------------------------------------------

@app.get('/Cliente', tags=[cliente_tag],
         responses={"200": ClienteViewSchema, "404": ErrorSchema})
def get_Cliente(query: ClienteBuscaSchema):
    """Faz a busca por um cliente a partir do nome do cliente

    Retorna uma representação do cliente encontrado
    """
    cliente_nome = query.nome
    logger.debug(f"Coletando dados sobre o cliente #{cliente_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    cliente = session.query(Cliente).filter(func.lower(Cliente.nome) == cliente_nome.lower()).first()

    if not cliente:
        # se o cliente não foi encontrado
        error_msg = "Cliente não encontrado na base de dados:/"
        logger.warning(f"Erro ao buscar cliente '{cliente_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Cliente econtrado: '{cliente.nome}'")
        # retorna a representação de Cliente
        return apresenta_cliente(cliente), 200