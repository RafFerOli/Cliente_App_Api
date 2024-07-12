# Cliente APP API

Este pequeno projeto tem como objetivo realizar o controle de informações dos clientes de uma pequena empresa através de uma API desenvolvida seguindo o estilo REST.

O objetivo aqui é demonstrar parte do conhecimento adquirido durante a disciplina de **Arquitetura de Software** 

As principais tecnologias que foram utilizadas aqui são:

 - [Python](https://www.python.org/)
 - [Flask](https://flask.palletsprojects.com/en/2.3.x/)
 - [SQLAlchemy](https://www.sqlalchemy.org/)
 - [OpenAPI3](https://swagger.io/specification/)
 - [SQLite](https://www.sqlite.org/index.html)
 - [Docker](https://www.docker.com/)

---
### Instalação


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

---
### Executando o servidor


Para executar a API deve se ir via terminal até a pasta **"app"** e executar o seguinte comando comando:

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5000 --reload
```

---
### Acesso no browser

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

> Para executar o sistema completo será necessário fazer o download do projeto [Cliente App Front](https://github.com/RafFerOli/Fluxo_App_Front/tree/main), salvar a pasta Cliente_app_front e Cliente_app_api no mesmo diretório, abrir o diretório na IDE de sua escolha e seguir as instruções de [README.md](https://github.com/RafFerOli/Cliente_App_Front/blob/main/Cliente_app_front/README.md).

---
## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal. Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t cliente-api .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -p 5000:5000 cliente-api
```

Uma vez executando, para acessar a API, basta abrir o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador.

### Alguns comandos úteis do Docker

>**Para criar uma imagem** você pode executar o seguinte comando:
>
>```
>$ docker build -t <IMAGE NAME> .
>```
>Subistituindo o `IMAGE NAME` pelo nome da imagem que se deseja criar
>
>**Para executar um container** você pode executar o seguinte comando:
>
>```
>$ docker run -d -p <PORT> <IMAGE NAME> .
>```
>Subistituindo o `IMAGE NAME` pelo nome da imagem desejada e `PORT` pela porta de acesso desejada.
>
>**Para verificar se a imagem foi criada** você pode executar o seguinte comando:
>
>```
>$ docker images
>```
>
> Caso queira **remover uma imagem**, basta executar o comando:
>```
>$ docker rmi <IMAGE ID>
>```
>Subistituindo o `IMAGE ID` pelo código da imagem
>
>**Para verificar se o container está em exceução** você pode executar o seguinte comando:
>
>```
>$ docker container ls --all
>```
>
> Caso queira **parar um conatiner**, basta executar o comando:
>```
>$ docker stop <CONTAINER ID>
>```
>Subistituindo o `CONTAINER ID` pelo ID do conatiner
>
>
> Caso queira **destruir um conatiner**, basta executar o comando:
>```
>$ docker rm <CONTAINER ID>
>```
>Para mais comandos, veja a [documentação do docker](https://docs.docker.com/engine/reference/run/).
