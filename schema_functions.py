"""Ferramentas de manuseio e Inicializaçao do Banco de dados."""

from tinymongo import TinyMongoClient
from schema import Elemento, init_Elementos, init_Pesquisa


def init_BancoDeDados(elementos: list):
    """Adição dos elementos no banco de dados."""
    connection = TinyMongoClient()
    database = connection.database
    collection = database.elementos

    for elemento in elementos:
        collection.insert_one({
                              'sigla': elemento.sigla,
                              'nome': elemento.nome,
                              'familia': elemento.familia,
                              'atomico': elemento.atomico,
                              'm_molar': elemento.m_molar
                              }
                              ).inserted_id


def init_system():
    """Inicializa a lista de pesquisa e o Banco de dados."""
    elementos = init_Elementos()
    init_Pesquisa(elementos)
    # init_BancoDeDados(elementos)

def jsonToElemento(json: dict) -> Elemento:
    """
    Trata o dado retornado pelo banco de dados.

    Transforma o retorno do banco de dados que é em json mas tratado em python
    como dict, para uma de instância Elemento.
    """
    elemento = Elemento(
                        json.get('sigla'),
                        json.get('nome'),
                        json.get('familia'),
                        json.get('atomico'),
                        json.get('m_molar')
                       )
    return elemento


def buscaElemento_Sigla(chave: str) -> Elemento:
    """Busca a sigla do elemento no banco de dados."""
    connection = TinyMongoClient()
    database = connection.database
    collection = database.elementos
    info = collection.find_one({'sigla': chave})

    return jsonToElemento(info)


def buscaElemento_Nome(chave: str) -> Elemento:
    """Busca o nome do elemento no banco de dados."""
    connection = TinyMongoClient()
    database = connection.database
    collection = database.elementos
    info = collection.find_one({'nome': chave})

    return jsonToElemento(info)
