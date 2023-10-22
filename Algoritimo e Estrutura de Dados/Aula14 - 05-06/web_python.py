from bs4 import BeautifulSoup
import requests

url = "https://www.python.org"

dados = requests.get(url)
#print(dados.content) #TRAZ O CODIGO COMPLETO

html = BeautifulSoup(dados.content, "html.parser")#faz um "parser"(conversao ) para um codigo html "mais legiivel"

#print (html.prettify())#exibe todo o codigo html da pagina

#================================================================
#ATIVIDADE => TRAZER AS INFORMACOES DA TAG UL
listas= html.find_all("ul", class_="menu")#pega TODOS os elementos da tag ul da class menu e adiciona a variavel listas
#print(listas)
noticias = listas[15].find_all("li")

#print(noticias)

for noticia in noticias:
    print(noticia.a.string)
