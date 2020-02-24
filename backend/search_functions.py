"""Ferramentas de busca de elementos, no banco de dados."""
import re
from unidecode import unidecode
from typing import List
from schema import Elemento
from schema_functions import buscaElemento_Sigla,\
    buscaElemento_Nome


def temAcento(palavra: str) -> bool:
    """Checa se a palavra usada no parâmetro contém algum acento."""
    acentoMaiuscula = 'ÁÉÍÓÚÂÊÎÔÛÃẼĨÕŨ'

    acentoMinuscula = 'áéíóúâêîûãẽĩõũ'
    for count in range(len(acentoMaiuscula)):
        if acentoMaiuscula[count] in palavra:
            return True
    for count in range(len(acentoMinuscula)):
        if acentoMinuscula[count] in palavra:
            return True
    return False


def find_sigla(chave: str, elementos: List):
    """Realiza a pesquisa do elemento pela sigla."""
    for count in range(118):
        pesquisa = re.search(chave, elementos[count].sigla)
        if pesquisa is not None:
            return elementos[count].sigla
    return -1


def find_nome(chave: str, elementos: List):
    """Realiza a pesquisa do elemento pelo nome."""
    print(chave)
    for count in range(118):
        if temAcento(chave):
            pesquisa = re.search(chave, elementos[count].nome)
        else:
            pesquisa = re.search(chave, unidecode(elementos[count].nome))
        if pesquisa is not None:
            print(pesquisa, count)
            return elementos[count].nome

    return None


def retornaChave(chave):
    """Deixa a chave de forma apropriada para pesquisa."""
    if len(chave) <= 0:
        return False
    # Coloca a primeira letra da string como maiuscula
    return chave.capitalize()


def busca(chave: str, elementos: list) -> Elemento:
    """Função que realiza a busca no banco de dados."""
    # Realiza a verificação se foi escrito algo valido
    chave = retornaChave(chave)
    if chave is False:
        return None
    tamanho = len(chave)
    # Checa se é uma sigla ou nome de um elemento
    if tamanho <= 2:
        resultado = find_sigla(chave, elementos)
        if resultado is not None:
            return buscaElemento_Sigla(resultado)
    else:
        resultado = find_nome(chave, elementos)
        if resultado[0] is not None:
            return buscaElemento_Nome(resultado)
    return None
