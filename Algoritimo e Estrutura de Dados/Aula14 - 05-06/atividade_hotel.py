from bs4 import BeautifulSoup
import requests

url = "https://www.hotel.com.br/hoteis-em-pelotas.html"

dados = requests.get(url)
#print(dados.content)

html = BeautifulSoup(dados.content, "html.parser")# faz um "parser" (conversao ) para um codigo html "mais legivel"

def lista_hoteis():
	nomes = html.find_all("h2")
	enderecos = html.find_all("h3")
	diarias = html.find_all("strong")
	for hotel, endereco, diaria in zip(nomes, enderecos, diarias):
		print(f"NOME DO HOTEL: {hotel.string}\nENDERECO: {endereco.string}\nPRECO DIARIA:{diaria.string}\n")

def pesq_endereco():
	endereco_pesq = input("Qual o endereco de busca: ")
	enderecos = html.find_all("h3")
	encontrado = False
	for endereco in enderecos:
		if endereco_pesq.lower() in endereco.lower():
				if encontrado == False:
					encontrado = True
				print(endereco.string)
	if encontrado == False:
		print()
		print("Nao foi encontrado!!")
		print()


def listar_ordem_valor():
	diarias_valores = []

	diarias = html.find_all("strong")
	for diaria in diarias:
		diarias_valores.append(diaria)

	for ordem in range(diarias_valores,0,-1):
		print(ordem)

while True:
	print("1. Listar Hoteis(nome, endereco, diaria)")
	print("2. Pesquisar por endereco (ou parte)")
	print("3. Listar em ordem de valor da diaria")
	print("4. Finalizar")

	opt = int(input('Digite a opcao desejada: '))

	if opt == 1:
		lista_hoteis()
	elif opt == 2:
		pesq_endereco()
	elif opt == 3:
		listar_ordem_valor()
	elif opt == 4:
		break
	else:
		break
