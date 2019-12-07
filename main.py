"""
Programa de busca de elementos quimicos
Autor: Alexandre Fernandes dos Santos.
"""

from schema import *
from schema_function import *


def find_sigla(chave):
    """Realiza a pesquisa do elemento pela sigla."""
    count_1, count_2 = 0, 0
    tamanho = len(chave)
    for count_1 in range(118):
        similaridade = 0
        if len(list_elements[count_1].sigla) != tamanho:
            continue
        for count_2 in range(tamanho):
            if list_elements[count_1].sigla[count_2] == chave[count_2]:
                similaridade += 1
                if similaridade == tamanho:
                    return count_1
    return -1


def find_nome(chave):
    """Realiza a pesquisa do elemento pelo nome."""
    count = 0
    # Provavel armazena primeiro se
    # a similaridade e valida, posicao e a similaridade
    provavel = [0, 0, 0]
    for count in range(118):
        similaridade = eIgual(chave, list_elements[count].nome)
        if similaridade is True:
            provavel[0] = 1
            provavel[1] = count
            return provavel
        if similaridade > provavel[2]:
            provavel[1] = count
            provavel[2] = similaridade
    # Parametro de razoabilidade para ser igual
    if provavel[2] > 3:
        provavel[0] = 2

    return provavel


def eVogal(aux):
    """Checa se é uma vogal e que vogal."""
    aux.lower()
    vogalA = ['a', 'á', 'â', 'ã']
    vogalE = ['e', 'é', 'ê']
    vogalI = ['i', 'í']
    vogalO = ['o', 'ó', 'ô', 'õ']
    vogalU = ['u', 'ú']

    if aux in vogalA:
        return 1
    if aux in vogalE:
        return 2
    if aux in vogalI:
        return 3
    if aux in vogalO:
        return 4
    if aux in vogalU:
        return 5

    return False


def comparaLetras(letraA, letraB):
    """Compara se a letraA, é igual a letraB."""
    if letraA == letraB:
        return True
    vogalA = eVogal(letraA)
    vogalB = eVogal(letraB)

    if vogalA is True and vogalB is True:
        return True if vogalA == vogalB else False

    return False


def eIgual(chave, aux):
    """Checa se a chave de pesquisa é igual a aux."""
    similaridade = 0
    tamanho = len(chave)
    percorrer = len(aux)
    if (tamanho < percorrer):
        percorrer = tamanho

    for count in range(percorrer):
        if comparaLetras(chave[count], aux[count]):
            similaridade += 1

        tamanho = len(aux)
        if similaridade == tamanho:
            print("\nChaveTrue", chave, "aux", aux, "similaridade", similaridade)
            return True
    print("\nChave", chave, "aux", aux, "similaridade", similaridade)
    return similaridade if similaridade >= tamanho / 3 else 0


def retornaChave(pesquisa):
    """Deixa a chave de forma apropriada para pesquisa."""
    if len(pesquisa) <= 0:
        return False
    # Coloca a primeira letra da string como maiuscula
    if pesquisa[0] >= "a":
        aux = (pesquisa[0:1].upper()) + pesquisa[1:]
    else:
        aux = pesquisa
    return aux


def busca(e):
    """Função que realiza a busca no banco de dados."""
    # Realiza a verificação se foi escrito algo valido
    pesquisado = retornaChave(pesquisa.get())
    if pesquisado is False:
        resposta.set("Aguardando Pesquisa")
        return
    # Checa se é valido e também uma string
    if type(pesquisado) == str:
        tamanho = len(pesquisado)
        count = 0
    # Checa se é uma sigla ou nome de um elemento
        if tamanho <= 2:
            result_find = find_sigla(pesquisado)
            if result_find != -1:
                resposta.set(list_elements[result_find])
                return
        else:
            result_find = find_nome(pesquisado)
            if result_find[0] != 0:
                resposta.set(list_elements[result_find[1]])
                return
        resposta.set("Por favor digite a sigla ou\n o nome do elemento novamente")
        return


# Processamento principal
# Inicializaçao da estrutura dos dados e da interface
from tkinter import *
app = Tk()
app.geometry("250x220+800+400");
app.title ('Tabela de Elementos')
Label(app, text = "Digite um elemento a ser procurado").pack(padx = "20", pady = "10");
pesquisa = Entry(app)
pesquisa.pack(padx = "25", pady ="30")
#Button(app, text = "Buscar", command = busca).pack(padx = "10", pady ="15");
resposta = StringVar()
resposta.set("Aguardando Pesquisa")
resultado = Label(app, textvariable = resposta).pack(pady="7");

list_elements = init_Elementos()
app.bind("<Key>", busca);
app.mainloop()
