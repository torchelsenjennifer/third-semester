import requests
from bs4 import BeautifulSoup

url_kabum = 'https://www.kabum.com.br/busca/monitor-lg'
kabum = requests.get(url_kabum)

soup = BeautifulSoup(kabum.text, 'html.parser')

produtosKabum = soup.find_all("div", class_="productCard")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>> KABUM <<<<<<<<<<<<<<<<<<<<<<<<<<")
for produto in produtosKabum:
    nome = produto.find("span", class_="nameCard").text
    preco = produto.find("span", class_="priceCard").text
    print("nome: ", nome)
    print("preco: ", preco)

url_submarino = "https://www.submarino.com.br/busca/monitor-lg"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

submarino = requests.get(url_submarino, headers=headers)
soup = BeautifulSoup(submarino.text, 'html.parser')

produtosSub = soup.find_all("a", class_="inStockCard__Link-sc-1ngt5zo-1")


print(">>>>>>>>>>>>>>>>>>>>>>>>>>> SUBMARINO <<<<<<<<<<<<<<<<<<<<<<<<<<")
for produto in produtosSub:
    nome = produto.find("h3", class_="product-name__Name-sc-1shovj0-0").text
    preco = produto.find("span", class_="price__PromotionalPrice-sc-h6xgft-1").text
    print("nome: ", nome)
    print("preco: ", preco)
