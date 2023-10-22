import csv
jogadores = []

def carrega_dados():
    with open('football_players.csv', mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for linha in csv_reader:
            jogadores.append(linha)

def titulo(texto, sublinhado="-"):
    print()
    print(texto)
    print(sublinhado*40)

def listagem():
    titulo("Lista das Maiores Transferências")

    print("\nNome do Jogador..............: Clube de Origem....: Clube Destino......: Posição....:")

    for linha in jogadores:
        print(f"{linha['Player']:30} {linha['From(Club)']:20} {linha['To(Club)']:20} {linha['Position']}")

def agrupar_pais():
    titulo("Nº de Transferências por País de Origem do Jogador")

    dicionario = {}
    for jogador in jogadores:
        # busca a palavra (chave). Se não existir: None
        num = dicionario.get(jogador["Origin"], None)
        if num == None:
            # não existe, adiciona com o valor 1
            dicionario[jogador["Origin"]] = 1
        else:
            # se existe, adiciona mais 1 ao valor
            dicionario[jogador["Origin"]] = num + 1

    # classifica os dados do dicionário em uma lista
    lista = sorted(dicionario.items(), key=lambda dic : dic[1], reverse=True)
#    print(lista)

    print("\nPaís de Origem do Jogador  Nº de Transferências")

    # lista as chaves (países) e values (números)    
#    for (pais, num) in dicionario.items():
#        print(f"{pais:30} {num}")
        
    for (pais, num) in lista:
        print(f"{pais:30} {num}")

carrega_dados()

while True:
    titulo("Estatísticas: Transferências de Jogadores")    
    print("1. Listagem dos Jogadores")
    print("2. Listar em Ordem de Nome")
    print("3. Agrupar por País")
    print("4. Idades")
    print("5. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        listagem()
    elif opcao == 3:
        agrupar_pais()
    else:
        break
