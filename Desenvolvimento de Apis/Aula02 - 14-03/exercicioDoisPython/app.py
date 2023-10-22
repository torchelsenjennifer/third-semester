import requests
api_url = "http://localhost:3000/"

#=================================================================================================
#FUNCAO INCLUIR PRODUTO (CREATE)
def incluirProduto(descricao, marca, preco, quant): 
    try:
        todo = {"descricao": descricao, "marca": marca, "preco": preco, "quant": quant}
        response = requests.post(api_url + 'produtos', json=todo)
        if(response.status_code != 201):
            print('Erro no status code')
            return 
        print("Produto inserido com sucesso!!")
    except:
        print("Erro")

#===================================================================================================
#FUNCAO LISTAR PRODUTOS (READ)
def listarProdutos():
    try:
        response = requests.get(api_url + 'produtos')
        if(response.status_code != 200):
            print('Erro no status code')
            return 
        produtos = response.json()
        for produto in produtos:
             print(f"{produto.get('id')} {produto.get('descricao')}")
    except:
        print("Erro")

#=====================================================================================================
#FUNCAO ALTERAR PRODUTOS (UPDATE)
def alterarProduto(id, descricao, marca, preco, quant):
    try:
        todo = {"descricao":descricao, "marca": marca, "preco": preco, "quant":quant}
        response = requests.put(api_url + 'produtos/' + f"{id}", json=todo)
        if(response.status_code != 200):
                print('Erro no status code')
                return
        print("\nAlterado com sucesso")
    except:
        print('Erro')


#=====================================================================================================
#FUNCAO EXCLUIR PRODUTO(DELETE)
def excluirProduto(exclusao):
    try:
        response = requests.delete(api_url + 'produtos/' + f'{exclusao}')
        if(response.status_code != 200):
            print('Erro no status code')
            return
        print("Excluido com sucesso!!")
    except:
        print("Erro")
#=============================================================================================
#FUNCAO PESQUISAR
def pesquisarProduto(id):
      
    try:
        response = requests.get(api_url + 'produtos/' + f"{id}")
        if(response.status_code != 200):
            print('Erro no status code')
            return 
        produto = response.json()
        print(f"Descrição: {produto.get('descricao')}")
        print(f"Marca: {produto.get('marca')}")
        print(f"Preco R$: {produto.get('preco'):6.2f}")
        print(f"Quantidade: {produto.get('quant')}")
    except:
        print("Erro")
#===============================================================================================
#FUNCAO TOTAL
def total():
    try:
        response = requests.get(api_url + 'produtos/total')
        if(response.status_code != 200):
            print('Erro no status code')
            return 
        produto = response.json()
        print(f"Produtos Cadastrado: {produto.get('num')}")
        print(f"Soma dos Preços dos produtos Cadastrados: {produto.get('total'):6.2f}")
        print(f"Valor total do estoque: {produto.get('total2'):6.2f}")
    except:
        print("Erro")
#===================================================================================================
#MENU
while(True):

    print()   
    print("Produto")
    print("-"*30)
    print("1. Incluir ")
    print("2. Listar ")
    print("3. Alterar")
    print("4. Excluir")
    print("5. Pesquisar")
    print("6. Total")
    print("7. Finalizar")
    print()

    opcao = int(input("Opção: "))

    if( opcao == 1):
        print("Voce acessou para incluir(descricao, marca, preco e quant)")
        descricao = input("Descricao do Produto: ")
        marca = input("Marca do Produto: ")
        preco = float(input("Preço do Produto: "))
        quant = int(input("Quantidade do Produto: "))
        incluirProduto(descricao, marca, preco, quant)
       
    if( opcao == 2 ):
        listarProdutos()

    if( opcao == 3):
        id = int(input("Qual o produto que deseja alterar: "))
        print()
        print("Atualize as informações")
        descricao = input("Descricao do Produto: ")
        marca = input("Marca do Produto: ")
        preco = float(input("Preço do Produto: "))
        quant = int(input("Quantidade do Produto: "))
        alterarProduto(id, descricao, marca, preco, quant)

    if( opcao == 4):
        exclusao = int(input("Qual o produto que deseja excluir: "))
        excluirProduto(exclusao)

    if(opcao == 5):
        id = int(input("Qual o produto que deseja pesquisar: "))
        print()
        pesquisarProduto(id)

    if(opcao == 6):
        total()

    if(opcao == 7):
       break