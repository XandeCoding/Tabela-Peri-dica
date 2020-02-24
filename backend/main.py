"""
Programa de busca e consulta de elementos químicos.

Autor: Alexandre Fernandes dos Santos.
"""
import graphene
from fastapi import FastAPI
from starlette.requests import Request
from starlette.graphql import GraphQLApp
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from configuration import elementos, local_directory
from schema_functions import buscaElemento_Nome, buscaElemento_Sigla
from schema_functions import buscaElemento_Familia
from search_functions import retornaChave, find_nome, find_sigla


app = FastAPI()

origins = ['*']

app.elementos = elementos
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['POST'],
    allow_headers=['*'])

app.mount('/static', StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')


class ElementoQL(graphene.ObjectType):
    """Declara os campos que são reconhecidos pelo graphql."""

    nome = graphene.String()
    sigla = graphene.String()
    familia = graphene.String()
    atomico = graphene.String()
    m_molar = graphene.String()


class Query(graphene.ObjectType):
    """Classe onde as Querys são declaradas e os Resolvers das mesmas."""

    elemento = graphene.Field(
               ElementoQL, name=graphene.String(default_value="stranger"))
    sigla = graphene.Field(
            ElementoQL, name=graphene.String(default_value="stranger"))
    familia = graphene.List(
              ElementoQL, name=graphene.String(default_value="stranger"))

    def resolve_elemento(parent, info, name):
        """Função que retorna os dados da querie de elemento."""
        resultado = find_nome(retornaChave(name), app.elementos)
        return buscaElemento_Nome(resultado)

    def resolve_sigla(parent, info, name):
        """Função que retorna os dados da querie de sigla."""
        resultado = find_sigla(retornaChave(name), app.elementos)
        return buscaElemento_Sigla(resultado)

    def resolve_familia(parent, info, name):
        """Função que retorna os dados da querie de familia."""
        lista = list()
        [lista.append(elemento)
            for elemento in buscaElemento_Familia(name)]
        return lista


app.add_route(
    '/graphql', GraphQLApp(schema=graphene.Schema(query=Query, auto_camelcase=False)))

@app.get('/')
async def search_elements(request: Request):
    print(local_directory)
    return templates.TemplateResponse('index.html', {'request': request})
