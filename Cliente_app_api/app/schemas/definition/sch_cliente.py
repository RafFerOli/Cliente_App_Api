from pydantic import BaseModel
from typing import Optional, List
from model.table.tb_cliente import Cliente

class ClienteSchema(BaseModel):
    """ Define como um novo cliente a ser inserido deve ser representado
    """
    nome: str = "Empresa 01"
    cnpj: str = "12.345.678.0001/90"
    razao: str = "Empresa ltda"
    endereco: str = "Rua sem entrada e sem saida"
    numero: int = "01"
    cidade: str = "Cidadelandia"
    estado: str = "NA"
    bairro: str = "Bairrotopia"
    cep: str = "01234-567"
    telefone: str = "(11)9-1234-5678"
    email: str = "empresa@software.com"

class ClienteViewSchema(BaseModel):
    """ Define como um cliente será retornado: cliente
    """
    id: int = 1
    nome: str = "Empresa 01"
    cnpj: str = "12.345.678.0001/90"
    razao: str = "Empresa ltda"
    endereco: str = "Rua sem entrada e sem saida"
    numero: int = "01"
    cidade: str = "Cidadelandia"
    estado: str = "NA"
    bairro: str = "Bairrotopia"
    cep: str = "01234-567"
    telefone: str = "(11)9-1234-5678"
    email: str = "empresa@software.com"

class ClienteBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do cliente.
    """
    nome: str = "Zézinho"

class ListagemClientesSchema(BaseModel):
    """ Define como uma listagem de clientes será retornada.
    """
    clientes:List[ClienteSchema]

class ClienteDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_cliente(cliente: Cliente):
    """ Retorna uma representação do cliente seguindo o schema definido em
        ClienteViewSchema.
    """
    return {
            "nome": cliente.nome,
            "cnpj": cliente.cnpj,
            "razao": cliente.razao, 
            "endereco":cliente.endereco,
            "numero":cliente.numero,
            "cidade":cliente.cidade,
            "estado":cliente.estado,
            "bairro":cliente.bairro,
            "cep":cliente.cep,
            "telefone":cliente.telefone,
            "email":cliente.email
    }

def apresenta_clientes(clientes: List[Cliente]):
    """ Retorna uma representação dos clientes seguindo o schema definido em
        ClienteSchema(BaseModel):
    """
    result = []
    for cliente in clientes:
        result.append({
            "id": cliente.id,
            "nome": cliente.nome,
            "cnpj": cliente.cnpj,
            "razao": cliente.razao, 
            "endereco":cliente.endereco,
            "numero":cliente.numero,
            "cidade":cliente.cidade,
            "estado":cliente.estado,
            "bairro":cliente.bairro,
            "cep":cliente.cep,
            "telefone":cliente.telefone,
            "email":cliente.email
        })

    return {"clientes": result}
