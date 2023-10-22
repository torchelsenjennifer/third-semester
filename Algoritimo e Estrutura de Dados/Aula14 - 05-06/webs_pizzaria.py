from bs4 import BeautifulSoup
import requests

url = "https://edeciofernando.github.io/pizzaria/"

dados = requests.get(url) #busca o html da pagina

html = BeautifulSoup(dados.content, "html.parser") #faz um "parser" (conversao ) para um codigo html "mais legivel"

#print (html.prettify()) #exibe todo o codigo html da pagina

#=====================================================================
#TRAZ A INFORMACAO JUNTO COM O HTML
#print(html.title) #traz o titulo da página
#print(html.p) #traz o primeiro paragrafo do html
#print(html.ul) #traz a pimeira lista nao ordenada

#======================================================================
#TRAZ APENAS O TEXTO DENTRO DA TAG HTML
#print(html.title.string) #traz só o texto que esta dentro da tag
#print(html.p.string) #traz só o texto do primeiro paragrafo do html
#print(html.ul.li.string) #traz só o texto da primeirA elemneto li

#=====================================================================
#FIND_ALL() => [] TRAZ UM ARRAY(LISTA) E RETORNA UMA LISTA
#find_all(): busca todas as ocorrencias da tag e retorna uma lista
#listas = html.find_all("ul") #traz todos as tags com os seus conteudos
#print(listas)#mostra todos as tags com os seus conteudos

#=====================================================================
#FIND() => TRAZ A PRIMEIRA OCORRENCIA DA TAG E RETORNA UMA STRING
#find(): busca primeira ocorrencias e retorna uma string
#lista = html.find("ul")
#print(lista)

#links = lista.find_all("li")
#for link in links:
    #print(link.string) #lista os texto dentro da tag ul

#======================================================================
#traz os elementro de LI em texto
#lista = html.find_all("ul")

#print('='*40)
#diferenciais = lista[1].find_all("li")
#print(diferenciais)

#for dif in diferenciais:
#     print(dif.string) #traz os elementro de LI em texto

#=====================================================================
#TRAZ A INFORMACAO DA TAG SECTION COM ID
#print('='*40)
section_final = html.find("section", id="contato")
print(section_final.p.string)

#======================================================================