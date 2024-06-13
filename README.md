# Teste Globo

Este repositório contém 3 projetos pythons referentes ao teste ao processo seletivo da Globo. Ele foi desenvolvido na linguagem de programação python, consumindo uma API de Harry potter (https://wizard-world-api.herokuapp.com/Wizards):

Ele é divido nos seguintes módulos:

- Migration
- Prefect
- API

## Configuração

**Instalação de Dependências:**

Certifique-se de ter o Python instalado em sua máquina e o gerenciador de dependencias PIP. Este projeto utiliza as seguintes bibliotecas Python:

- httpx
- prefect
- prefect-sqlalchemy
- psycopg2-binary
- python-dotenv
- yoyo-migrations
- flask
- flask_sqlalchemy

Elas podem ser instaladas usando o commando abaixo do pip:

```bash
$ pip install -r requirements.txt
```

**Subindo o banco de dados**

Para subir o banco de dados é necessário ter docker instalado em sua maquina. Após isso, rode o seguinte comando abaixo na raiz do projeto para subir o banco.

```bash
$ docker-compose up -d
```

## Executando migration

O projeto foi desenvolvido usando a biblioteca yolo para gerenciamento de versões no banco de dados. Para rodar as migrations e sincronizar o banco de dados, navegue até a pasta migrator usando o seguinte comando:

```bash
$ cd migrator
```

Em seguida execute o script com:

```bash
$ python main.py
```

## Baixando os dados com prefector

Para rodar o prefector e baixar os dados, primeiro é necessário configurar um bloco. Para isso, estando na raiz do projeto, se direcione a pasta prefector rodando o comando abaixo:

```bash
$ cd prefect
```

Em seguida configure os blocos rodando:

```bash
$ python connector.py
```

Após isso, podemos executar nosso script com prefector usando:

```bash
$ python prefect_app.py
```

## API

A API do projeto foi desenvolvida usando a biblioteca FLASK e flask_sqlalchemy.

Para subir nossa API, ainda na raiz do projeto, se direcione a pasta api rodando o comando abaixo:

```bash
$ cd api
```

E rodamos usando:

```bash
$ python api.py
```

Sua aplicação subira no seguinte endereço:

http://127.0.0.1:5000

E voce poderá acessar usando as seguintes rotas

### Elixir

GET /elixirs: Retorna todos os elixires.

GET /elixirs/uuid:id: Retorna um elixir específico pelo ID.

POST /elixirs: Cria um novo elixir.

PUT /elixirs/uuid:id: Atualiza um elixir específico pelo ID.

DELETE /elixirs/uuid:id: Deleta um elixir específico pelo ID.

### Wizards

GET /wizards: Retorna todos os bruxos.

GET /wizards/uuid:id: Retorna um bruxo específico pelo ID.

POST /wizards: Cria um novo bruxo.

PUT /wizards/uuid:id: Atualiza um bruxo específico pelo ID.

DELETE /wizards/uuid:id: Deleta um bruxo específico pelo ID.

### Ingredients/

GET /ingredients: Retorna todos os ingredientes.

GET /ingredients/uuid:id: Retorna um ingrediente específico pelo ID.

POST /ingredients: Cria um novo ingrediente.

PUT /ingredients/uuid:id: Atualiza um ingrediente específico pelo ID.

DELETE /ingredients/uuid:id: Deleta um ingrediente específico pelo ID.
