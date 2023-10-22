from bs4 import BeautifulSoup
import requests

from exemplo import titulo

# titulo("Goleadores do Brasileirao 2023", "*")

url = "https://ge.globo.com/futebol/brasileirao-serie-a/"

conteudo = requests.get(url)

html = BeautifulSoup(conteudo.content, "html.parser")

goleadores = []

#===================================================================================================
def carregar_goleadores():
	div_jogadores = html.find_all("div", class_="ranking-item-wrapper")
	#print(div_jogadores[0])

	for div_jogador in div_jogadores:
		nome = div_jogador.find("div", class_="jogador-nome").string
		posicao = div_jogador.find("div", class_="jogador-posicao").string
		gols = div_jogador.find("div", class_="jogador-gols").string
		imagens = div_jogador.find_all("img")
		clube = imagens[1]["alt"]
		#print(nome, posicao, gols, clube)
		goleadores.append({"nome": nome, "posicao": posicao, "gols": gols, "clube": clube})
#=======================================================================================================

def listar():
	titulo("Listar por ordem de gols marcados", "=")

	print("Nome do Joagdor....: Clube..........: Posicao.............: Gols: ")
	print("-"*62)

	for goleador in goleadores:
		nome = goleador["nome"]
		clube = goleador["clube"]
		posicao = goleador["posicao"]
		gols = goleador["gols"]
		print(f"{nome:20} {clube:15} {posicao:20}  {gols}")


#=====================================================================================================
def listar_nome():
	titulo("Listar por ordem de nome do jogador", "=")

	print("Nome do Joagdor....: Clube..........: Posicao.............: Gols: ")
	print("-"*62)

	goleadores2 = sorted(goleadores, key=lambda goleador : goleador["nome"])

	for goleador in goleadores2:
		nome = goleador["nome"]
		clube = goleador["clube"]
		posicao = goleador["posicao"]
		gols = goleador["gols"]
		print(f"{nome:20} {clube:15} {posicao:20}  {gols}")

#==================================================================================================
def agrupar_clube():
	#dicionario = {"Botafogo": "Tiquinho Soares", "Flamengo": "Pedro, Arrascaeta"}
	dicionario = {}

	for goleador in goleadores:
		# busca a chave no dicionário e retorna None
		# se não existir
		nomes = dicionario.get(goleador["clube"], None)

		# se não existir a chave
		if nomes == None:
			# acrescenta uma chave no dicionario com o nome do jogador
			dicionario[goleador["clube"]] = goleador["nome"]
		else:
			# se ja existe, adiciona 1
			dicionario[goleador["clube"]] = nomes + ", " + goleador["nome"]

	goleadores2 = sorted(dicionario.items(), key=lambda dic : dic[0])

	titulo("Goleadores por Clube", "=")

	for(clube, nomes) in goleadores2:
		print(f"{clube}: {nomes}")

#====================================Programa Principal================================================
carregar_goleadores()
while True:
	titulo("Goleadores do Brasileirao 2023", "*")
	print("1. Listar Goleadores")
	print("2. Listar Goleadores em Ordem de Nome")
	print("3. Agrupar Goleadores por Clube")
	print("4. Finalizar")
	opcao = int(input("Opcao: "))
	match opcao:
		case 1:
			listar()
		case 2:
			listar_nome()
		case 3:
			agrupar_clube()
		case other:
			break