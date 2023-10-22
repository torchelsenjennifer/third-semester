from bs4 import BeautifulSoup
import requests

lista_gog = []
lista_steam = []
produtoPesq = ""

def carregar_dados():
    global produtoPesq
    teste = "Free to Play"
    teste2 = ""

    produtoPesq = input("Digite o produto: ")

    # Kabum -------------------------------
    url_gog = f"https://www.gog.com/en/games?query={produtoPesq}&order=desc:score"
    ulr_steam = "https://store.steampowered.com/search/?term=" + produtoPesq

    gog = requests.get(url_gog)
    steam = requests.get(ulr_steam)

    html_steam = BeautifulSoup(steam.content, "html.parser")
    html_gog = BeautifulSoup(gog.content, "html.parser")


    div_steam = html_steam.find_all("div", class_="responsive_search_name_combined")
    div_gog = html_gog.find_all("div", class_="product-tile__info")

    for produto in div_steam:
        nome = produto.find("span", class_="title").text.strip()
        tratar_preco = produto.find("div", class_="col search_price responsive_secondrow")

        if tratar_preco is not None:
            preco = tratar_preco.text.strip()

            if preco != "" and preco != "Free To Play" and preco != "Free to Play" and preco != "Free Demo" and preco != "Free":
                lista_steam.append({"nome": nome, "preco": preco})



    for produto in div_gog:
        nome = produto.find("span").text.strip()
        tratar_preco = produto.find("span", class_="final-value")

        if tratar_preco is not None:
            preco = tratar_preco.text.strip()
            if nome != 'DLC':
                lista_gog.append({"nome": nome, "preco": preco})

def titulo(msg, traco="="):
    print()
    print(msg)
    print(traco*50)

def listar_Steam():
    existe_jogo = False
    titulo(f"Lista de {produtoPesq.lower()} disponiveis na Kbum")

    print("Produto................................................................................................................................................: Preço.....:")

    for jogo in lista_steam:
        print(f"{jogo['nome']:150s}   {jogo['preco']}")
        existe_jogo = True

    if existe_jogo == False:
        print(f"Obs.: * Não há {produtoPesq} na Steam")

def listar_Gog():
    existe_jogo = False
    titulo(f"Lista de {produtoPesq.lower()} disponiveis na gog")


    print("Produto................................................................................................................................................: Preço.....:")

    for jogo in lista_gog:
        print(f"{jogo['nome']:150s}   R{jogo['preco']}")
        existe_jogo = True

    if existe_jogo == False:
        print(f"Obs.: * Não há {produtoPesq} na GoG")

def todos_produtos():
    todos = set()

    for jogo in lista_steam:
        todos.add(jogo['nome'])

    for jogo in lista_gog:
        todos.add(jogo['nome'])


    list = sorted(todos)

    for produto in list:
        print(produto)

def preco_steam():
    titulo(f"Lista de {produtoPesq.lower()} disponiveis na Steam")
    contador = 0
    valor_total = 0

    for jogo in lista_steam:
      print(f"{jogo['nome']:150s}   {jogo['preco']}")
      valor = float(jogo['preco'].replace('R$', '').replace(',', '.'))
      valor_total += valor
      contador += 1

    print()
    print(f"Valor total: ${valor_total}")
    print(f"Quantidade de jogos: {contador}")

def preco_gog():

    titulo(f"Lista de {produtoPesq.lower()} disponiveis na gog")
    contador = 0
    valor_total = 0
    for jogo in lista_gog:
        print(f"{jogo['nome']:150s}   R{jogo['preco']}")
        valor = float(jogo['preco'].replace('$', '').replace(',', '.'))
        valor_total += valor
        contador += 1

    print()
    print(f"Valor total: R${valor_total:.2f}")
    print(f"Quantidade de jogos: {contador}")

def diferentes_steam_gog():
    set_steam = set()
    set_gog = set()

    for produto in lista_steam:
        set_steam.add(produto['nome'])

    for produto in lista_gog:
        set_gog.add(produto['nome'])


    produtos_exclusivos_steam = set_steam.difference(set_gog)
    produtos_exclusivos_gog = set_gog.difference(set_steam)

    titulo(f"{produtoPesq} nas Lojas Steam e GOG: Exclusivos")

    if len(produtos_exclusivos_steam) > 0:
        print(f"Produtos exclusivos da Steam:")
        print()
        for produto in produtos_exclusivos_steam:
            print(produto)
        print()

    if len(produtos_exclusivos_gog) > 0:
        print(f"Produtos exclusivos da GOG:")
        print()
        for produto in produtos_exclusivos_gog:
            print(produto)
        print()

def comum_steam_gog():
    set_steam = set()
    set_gog = set()

    for produto in lista_steam:
        set_steam.add(produto['nome'])

    for produto in lista_gog:
        set_gog.add(produto['nome'])

    produtos_comuns = set_steam.intersection(set_gog)

    titulo(f"{produtoPesq} em Ambas as lojas")

    if len(produtos_comuns) == 0:
        print(f"Obs.: * Não há {produtoPesq} simultaneamente nas duas lojas")
    else:
        print("Esse jogo está disponível em ambas as lojas: ")
        print()
        print(":====================Steam====================:")
        print()
        for produto in set_steam:
            print(produto)
        print()
        print(":====================GoG====================:")
        print()
        for produto in set_gog:
            print(produto)

def fitro_preco():
    precoFiltrado = input("Digite o preço: ")
    jogos_encontrados_gog = False
    jogos_encontrados_steam = False

    print("===============Steam================")

    for produto in lista_steam:
        preco = produto['preco'].replace('R$', '').replace(',', '.')
        if precoFiltrado <= preco:
            print(produto['nome'])
            jogos_encontrados_steam = True
    if jogos_encontrados_steam == False:
        print("Não há jogos com esse preço na Steam")


    print("===============GoG================")

    for produto in lista_gog:
        preco = produto['preco'].replace('$', '').replace(',', '.')
        if precoFiltrado <= preco:
            print(produto['nome'])
            jogos_encontrados_gog = True

    if jogos_encontrados_gog == False:
        print("Não há jogos com esse preço na GoG")

carregar_dados()

while True:
    titulo("O que desejas saber?")
    print(f"1. {produtoPesq.capitalize()} na Steam")
    print(f"2. {produtoPesq.capitalize()} na gog")
    print(f"3. {produtoPesq.capitalize()} nas duas lojas")
    print(f"4. {produtoPesq.capitalize()} que não se repetem nas duas lojas")
    print(f"5. {produtoPesq.capitalize()} preco steam")
    print(f"6. {produtoPesq.capitalize()} preco gog")
    print(f"7. Filtrar por preço maior que")
    print(f"8. {produtoPesq.capitalize()} que não se repetem nas duas lojas")
    print("9. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        listar_Steam()
    elif opcao == 2:
        listar_Gog()
    elif opcao == 3:
        todos_produtos()
    elif opcao == 4:
        comum_steam_gog()
    elif opcao == 5:
        preco_steam()
    elif opcao == 6:
        preco_gog()
    elif opcao == 7:
        fitro_preco()
    elif opcao == 8:
        diferentes_steam_gog()
    else:
        print("Até mais")
        break
