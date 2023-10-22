import requests
api_url = "http://localhost:3000/produtos"

def titulo(texto, sublinhado="-"):
    print()
    print(texto)
    print(sublinhado*30)

def incluir():
    titulo("Inclusão de produtos")
    descricao = input("Descrição: ")
    marca = input("Marca...:")
    quant = int(input("Quantidade: "))
    preco = float(input("Preco R$: "))

    produto = {"descricao": descricao, 
               "marca": marca, 
               "quant": quant, 
               "preco": preco}
    
    response = requests.post(api_url, json=produto)
    if( response.status_code == 201):
        print('Ok. Produto Cadastrado com Sucesso')
        novo_produto = response.json()
        print(f"Codigo: {novo_produto['id']}")

def listar():
    titulo("Lista de produtos Cadastrado")
    response = requests.get(api_url)
    produtos = response.json()
    print("Cód. Descrição do produto ............... Marca: ....... Quant.  Preco:")
    for prod in produtos:
        print(f"{prod['id']:4d}", end=" ")
        print(f"{prod['descricao']:30}", end=" ")
        print(f"{prod['marca']:15}", end=" ")
        print(f"{prod['quant']:6d}", end=" ")
        print(f"{prod['preco']:9.2f}")

def alterar():
    titulo("Alteração de Produto")
    id = int(input("Código do Produto "))
    response = requests.get(api_url + "/"+str(id))
    produto = response.json()
    if produto['id'] == 0:
        print("Erro... Informe um Código Existente")
        return
    print("Informe os dados dos atributos a serem alterados. Sem alterção => Enter")

    print(f"Descrição: {produto['descricao']}")
    descricao = input("Descrição....:")

    print(f"Marca: {produto['marca']}")
    marca = input("Marca....:")

    print(f"Quantidade: {produto['quant']}")
    quant = input("Quantidade....:")

    print(f"Preco R$: {produto['preco']}")
    preco = input("Preco R$....:")

    desc_alt = descricao if descricao != "" else produto['descricao']
    marca_alt= marca if marca != "" else produto['marca']
    quant_alt= int(quant) if quant != "" else produto['quant']
    preco_alt= int(preco) if quant != "" else produto['preco']
 


def excluir():
    pass
def pesquisar():
    pass
def estatistica():
    pass

while True:
    titulo("Cadastro de Produtos - Consome API", "=")
    print("1. Inclusão")
    print("2. Listagem")
    print("3. Alteração")
    print("4. Exclusão")
    print("5. Pesquisa")
    print("6. Total")
    print("7. Finalizar")

    opcao = int(input("informe a sua opção: "))
    if opcao == 1:
        incluir()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        alterar()
    elif opcao == 4:
        excluir()
    elif opcao == 5:
        pesquisar()
    elif opcao == 6:
        estatistica()
    else:
        break

