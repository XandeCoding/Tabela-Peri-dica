"""
Programa de busca de elementos quimicos
Autor: Alexandre Fernandes dos Santos.
"""

from elementos import *

def find_sigla (chave):
	count_1 = 0
	count_2 = 0
	tamanho = len(chave)
	print("Tamanho da chave %d" % tamanho)
	for count_1 in range(118):
		similaridade = 0		
		if len(list_elements[count_1].sigla) != tamanho:
			continue		
		# print (list_elements[count_1].sigla)
		for count_2 in range(tamanho):			
			if list_elements[count_1].sigla[count_2] == chave[count_2]:
				similaridade+=1
				if similaridade == tamanho:
					print ("Similiraridade %d" % similaridade)				
					return count_1
	return -1

def find_nome (chave):
	count_1 = 0
	count_2 = 0
	# Provavel armazena primeiro se 
	# a similaridade e valida, posicao e a similaridade
	provavel = [0, 0, 0]
	tamanho = len(chave)	
	print("Tamanho da chave %d" % tamanho)
	for count_1 in range(118):
		similaridade = 0
		percorrer = len(list_elements[count_1].nome)
		if (tamanho < percorrer):
			percorrer = tamanho
		#print ("\nPercorrer e: %d" % percorrer)

		for count_2 in range(percorrer):			
			if list_elements[count_1].nome[count_2] == chave[count_2]:
				similaridade+=1
				if (similaridade > provavel[2]):
					provavel[1] = count_1
					provavel[2] = similaridade
				if (similaridade == tamanho
					and tamanho == percorrer):
					provavel[0] = 1
					return provavel


	if provavel[2] >= (tamanho/4):
		provavel[0] = 2

	return (provavel)

def busca (e):	
	aux = pesquisa.get()
	if (len(aux) <= 0):
		resposta.set ("Aguardando Pesquisa")
		return
	# Coloca a primeira letra da string como maiuscula
	if (aux[0] >= "a"):
		pesquisado = (aux[0:1].upper()) + aux[1:] 
		del (aux)
	else :
		pesquisado = aux
		del (aux)
	print("Palavra a ser pesquisada %s" % pesquisado)
	if type (pesquisado) == str:
		tamanho = len(pesquisado)
		count = 0
		if (tamanho <= 2):
			result_find = find_sigla (pesquisado)
			print ("Posicao na estrutura %d" % result_find)
			if (result_find != -1):
				resposta.set(list_elements[result_find])
				return

		else:
			result_find = find_nome (pesquisado)
			print (result_find)
			if (result_find[0] != 0):
				resposta.set(list_elements[result_find[1]])
				return

		resposta.set ("Por favor digite a sigla ou\n o nome do elemento novamente")
		return
			
	
# Processamento principal
# Inicializaçao da estrutura dos dados e da interface
from tkinter import *
app = Tk()
app.geometry("250x220+800+400");
app.title ('Tabela de Elementos')
Label(app, text = "Digite um elemento a ser procurado").pack(padx = "20", pady="10");
pesquisa = Entry(app)
pesquisa.pack(padx = "20", pady="0")
Button(app, text = "Buscar", command = busca).pack(padx = "10", pady="15");
resposta = StringVar()
resposta.set("Aguardando Pesquisa")
resultado = Label(app, textvariable = resposta).pack(pady="7");

list_elements = inicializa_estrutura()
app.bind("<Key>", busca);
app.mainloop()

