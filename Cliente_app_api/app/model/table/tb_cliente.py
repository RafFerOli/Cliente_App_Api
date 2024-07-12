from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

class Cliente(Base):    
    __tablename__ = 'cliente'

    id = Column("pk_cliente", Integer, primary_key=True)
    nome = Column(String(90), unique=True)
    cnpj = Column(String(19), unique=True)
    razao = Column(String(90))
    endereco = Column(String(90))
    numero = Column(String(7))
    cidade = Column(String(90))
    estado = Column(String(3))
    bairro = Column(String(90))
    cep = Column(String(10))
    telefone = Column(String(16))
    email = Column(String(90))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, cnpj:str, razao:str,
                 endereco:str,numero:int,cidade:str,estado:str,
                 bairro:str,cep:str,telefone:str,email:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cadastra um cliente

        Arguments:
            nome: nome do cliente.        
            cnpj: numero do cnpj do cliente
            razao: razão social cadastrada no sistema do estado
            endereco: endereço do cliente
            numero: = numero do logradouro do cliente
            cidade: = cidade do local da empresa do cliente
            estado: = estado do local da emrpesa do cliente
            bairro: = bairro dp local da empresa do cliente
            cep: = cep do local da empresa do cliente
            telefone: = telefone do cliente
            email: = email do cliente
        """       
        self.nome = nome
        self.cnpj = cnpj
        self.razao = razao
        self.endereco = endereco
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
        self.bairro = bairro
        self.cep = cep
        self.telefone = telefone
        self.email = email

        # se não for informada, será a data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

