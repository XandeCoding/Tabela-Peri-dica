"""
Programa de busca de elementos quimicos
Autor: Alexandre Fernandes dos Santos.
"""

from elementos import *

def find_sigla (chave):
	count_1 = 0
	count_2 = 0
	tamanho = len(chave)
	#print("Tamanho da chave %d" % tamanho)
	for count_1 in range(118):
		similaridade = 0		
		if len(list_elements[count_1].sigla) != tamanho:
			continue		
		# print (list_elements[count_1].sigla)
		for count_2 in range(tamanho):			
			if list_elements[count_1].sigla[count_2] == chave[count_2]:
				similaridade+=1
				if similaridade == tamanho:
					#print ("Similiraridade %d" % similaridade)				
					return count_1
	return -1

def find_nome (chave):
	count = 0
	# Provavel armazena primeiro se 
	# a similaridade e valida, posicao e a similaridade
	provavel = [0, 0, 0]
	
	#print("Tamanho da chave %d" % tamanho)
	for count in range(118):
		#print ("\nPercorrer e: %d" % percorrer)
		similaridade = eIgual(chave, list_elements[count].nome)
		if (similaridade == True):
			print ("entrou", similaridade)
			provavel[0] = 1
			provavel[1] = count
			return provavel				
		if (similaridade > provavel[2]):
			provavel[1] = count
			provavel[2] = similaridade
		

	#Parametro de razoabilidade para ser igual
	if provavel[2] != 0:
		provavel[0] = 2

	return (provavel)

def eVogal (aux):
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

def comparaLetras (letraA, letraB):
	if letraA == letraB:
		return True
	vogalA = eVogal (letraA)
	vogalB = eVogal (letraB)

	if (vogalA != False and vogalB != False):
		return True if vogalA == vogalB else False

	return False

def eIgual (chave, aux):
	similaridade = 0
	tamanho = len(chave)
	percorrer = len(aux)
	if (tamanho < percorrer):
		percorrer = tamanho

	for count in range(percorrer):
		if comparaLetras(chave[count], aux[count]):
			similaridade+=1

	tamanho = len(aux)
	if similaridade == tamanho:
		print ("\nChaveTrue",chave, "aux", aux, "similaridade", similaridade)
		return True
	print ("\nChave",chave, "aux", aux, "similaridade", similaridade)
	return similaridade if similaridade >= tamanho/ 3 else 0


def retornaChave (pesquisa):
	if (len(pesquisa) <= 0):
		return False
	# Coloca a primeira letra da string como maiuscula
	if (pesquisa[0] >= "a"):
		aux = (pesquisa[0:1].upper()) + pesquisa[1:] 
	else :
		aux = pesquisa
	return aux

def busca (e):	
	pesquisado = retornaChave(pesquisa.get())
	if (pesquisado == False):		
		resposta.set ("Aguardando Pesquisa")
		return
	#print("Palavra a ser pesquisada %s" % pesquisado)
	if type (pesquisado) == str:
		tamanho = len(pesquisado)
		count = 0
		if (tamanho <= 2):
			result_find = find_sigla (pesquisado)
			#print ("Posicao na estrutura %d" % result_find)
			if (result_find != -1):
				resposta.set(list_elements[result_find])
				return

		else:
			result_find = find_nome (pesquisado)
			#print (result_find)
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
Label(app, text = "Digite um elemento a ser procurado").pack(padx = "20", pady = "10");
pesquisa = Entry(app)
pesquisa.pack(padx = "25", pady ="30")
#Button(app, text = "Buscar", command = busca).pack(padx = "10", pady ="15");
resposta = StringVar()
resposta.set("Aguardando Pesquisa")
resultado = Label(app, textvariable = resposta).pack(pady="7");

list_elements = inicializa_estrutura()
app.bind("<Key>", busca);
app.mainloop()

