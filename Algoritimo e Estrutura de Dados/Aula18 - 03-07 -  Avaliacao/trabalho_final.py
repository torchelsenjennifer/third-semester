import requests
from bs4 import BeautifulSoup
from definicao import titulo

todosKabum = []
todosSubmarino = []
busca = ""

def carrega_dados():
	global busca
#=================================================================
	busca = input("Por favor, Digite o nome do produto: ")
#=================================================================

	url_kabum = 'https://www.kabum.com.br/busca/' + busca
	kabum = requests.get(url_kabum)

	soup = BeautifulSoup(kabum.text, 'html.parser')

	produtosKabum = soup.find_all("div", class_="productCard")
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>> KABUM <<<<<<<<<<<<<<<<<<<<<<<<<<")
	for produto in produtosKabum:
		nome = produto.find("span", class_="nameCard").text
		preco = produto.find("span", class_="priceCard").text
		div_desconto = produto.find("div", class_="sc-d55b419d-5 fXfHSb discountTagCard")
		#print(div_desconto)
		desconto = int(div_desconto.findChildren("p")[0].text.replace("%", "")) if div_desconto != None else 0
		#print(desconto)
		todosKabum.append({"nome": nome, "preco": preco, "desconto": desconto, "origem": "KABUM" })
		#print("nome: ", nome)
		#print("preco: ", preco)


	url_submarino = "https://www.submarino.com.br/busca/" + busca
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

	submarino = requests.get(url_submarino, headers=headers)
	soup = BeautifulSoup(submarino.text, 'html.parser')

	produtosSub = soup.find_all("a", class_="inStockCard__Link-sc-1ngt5zo-1")


	print(">>>>>>>>>>>>>>>>>>>>>>>>>>> SUBMARINO <<<<<<<<<<<<<<<<<<<<<<<<<<")
	for produto in produtosSub:
		nome = produto.find("h3", class_="product-name__Name-sc-1shovj0-0").text
		preco = produto.find("span", class_="price__PromotionalPrice-sc-h6xgft-1").text
		span_desconto = produto.find("span", class_="discount-badge__Text-sc-s5bp91-2 YfKws")
		#print(span_desconto)
		desconto = int(span_desconto.text.replace("%", "")) if span_desconto != None else 0
		#print(desconto)
		todosSubmarino.append({"nome": nome, "preco": preco, "desconto": desconto, "origem": "SUBMARINO"})
		#print("nome: ", nome)
		#print("preco: ", preco)

def listar_kabum():
	titulo("Listar de produtos na Loja Kabum", "=")
	print("PRODUTO......................................................................................................................................: PRECO:............ ")
	for todoKabum in todosKabum:
		nome = todoKabum["nome"]
		preco = todoKabum["preco"]

		print(f"{nome:150} {preco:10}")


def listar_submarino():
	titulo("Listar de produtos na Loja Submarino", "=")
	print("PRODUTO......................................................................................................................................: PRECO:............ ")

	for todoSubmarino in todosSubmarino:
		nome =  todoSubmarino["nome"]
		preco = todoSubmarino["preco"]
		print(f"{nome:150} {preco:10}")


def listar_desconto_kabum():
	titulo("Listar por maior desconto no Loja Kabum", "=")
	print("PRODUTO........................................................................................................................................: PRECO:............ Desconto:.........")

	ordenar_maior_desconto = sorted(todosKabum, key=lambda todoKabum : todoKabum["desconto"], reverse=True)

	for todoKabum in ordenar_maior_desconto:
		nome = todoKabum["nome"]
		preco = todoKabum["preco"]
		desconto = todoKabum["desconto"]
		print(f"{nome:145} {preco:15} {desconto:7}%")

def listar_desconto_submarino():
	titulo("Listar por maior desconto no Loja Submarino", "=")
	print("PRODUTO........................................................................................................................................: PRECO:............ Desconto:.........")

	ordenar_maior_desconto = sorted(todosSubmarino, key=lambda todoSubmarino : todoSubmarino["desconto"], reverse=True)

	for todoSubmarino in ordenar_maior_desconto:
		nome = todoSubmarino["nome"]
		preco = todoSubmarino["preco"]
		desconto = todoSubmarino["desconto"]
		print(f"{nome:145} {preco:15} {desconto:7}%")

def uniao_kabum_submarino():
	titulo("Uniao entre lojas, Kabum x Submarino", "=")
	set_kabum = set()
	set_submarino = set()

	for todoKabum in todosKabum:
		set_kabum.add({
			"nome": todoKabum["nome"]
		})

	for todoSubmarino in todosSubmarino:
		set_submarino.add({
			"nome": todoSubmarino["nome"]
		})

	uniaoProdutos = set_kabum.union(set_submarino)

	if len(uniaoProdutos) == 0:
		print("Nao itens em comum!")
	else:
		for roberto in uniaoProdutos:
			print(roberto["nome"])

def totalizacao_Kabum():
	print("Quantidade total de produtos disponiveis na KABUM")
	total_preco = 0
	itens = 0
	media_preco = 0

	for todoKabum in todosKabum:
		valor = float(todoKabum['preco'].replace('R$', '').replace(',', '.'))
		total_preco += valor
		itens += 1

	media_preco = (total_preco/itens)
	print()
	print(f"Media total de itens: ${media_preco}")
	print(F"Total de itens da pesquisa: {itens}")

def totalizacao_Submarino():
	print("Quantidade total de produtos disponiveis na KABUM")
	total_preco = 0
	itens = 0
	media_preco = 0

	for todoKabum in todosKabum:
		valor = float(todoKabum['preco'].replace('R$', '').replace(',', '.'))
		total_preco += valor
		itens += 1

	media_preco = (total_preco/itens)
	print()
	print(f"Media total de itens: ${media_preco}")
	print(F"Total de itens da pesquisa: {itens}")


def pesq_lojas():
	print("")

carrega_dados()
#====================================Programa Principal================================================
#
while True:
	titulo("Kabum versus Submarino ", "*")
	print("1. Listar " + busca + " da loja Kabum ")
	print("2. Listar " + busca + " da loja Submarino ")
	print("3. Listar " + busca + " por desconto na Kabum ")
	print("4. Listar " + busca + " por desconto na submarino ")
	print("5. Comparacao de valores, Kabum x Submarino ")
	print("6. Totalizacao na Loja Kabum ")
	print("7. Totalizacao na Loja Submarino ")
	print("8. Pesquisa ")
	print("9. Finalizar")
	opcao = int(input("VEJA O MENU E SELECIONE UM NUMERO: "))
	match opcao:
		case 1:
			listar_kabum()
		case 2:
			listar_submarino()
		case 3:
			listar_desconto_kabum()
		case 4:
			listar_desconto_submarino()
		case 5:
			uniao_kabum_submarino()
		case 6:
			totalizacao_Kabum()
		case 7:
			totalizacao_Submarino()
		case 8:
			pesq_lojas()
		case 9:
			break
		case other:
			break