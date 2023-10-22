# utilizando conjuntos e listas criar um programa para cadastrar artilheiros, com o seguinte menu:
gauchao = set()
brasileirao = set()

def incluir_gauchao():
    nome = input('Digite o nome do artilheiro: ')
    gauchao.add(nome)
    print('Artilheiro cadastrado com sucesso!')

def incluir_brasileirao():
    nome = input('Digite o nome do artilheiro: ')
    brasileirao.add(nome)
    print('Artilheiro cadastrado com sucesso!')

def listar_artilheiros():
    print('Artilheiros do Gauchão: ')
    for i in gauchao:
        print(i)
    print('Artilheiros do Brasileirão: ')
    for i in brasileirao:
        print(i)
    print('Artilheiros: ')
    for i in gauchao | brasileirao:
        print(i)

def artilheiros_campeonatos():
    print(gauchao & brasileirao)

def artilheiros_gauchao():
    print(gauchao - brasileirao)

def artilheiros_um_campeonato():
    artilheiros=gauchao ^ brasileirao
    for i in artilheiros:
      print(i, end=' ')

def listar_artilheiros_ordem():
    print(sorted(gauchao | brasileirao))


while True:
    print('''
    1 - Incluir artilheiro Gauchão
    2 - Incluir artilheiro Brasileirão
    3 - Listar artilheiros
    4 - Artilheiros nos 2 campenatos
    5 - Marcou apenas no Gauchão
    6 - Marcou apenas em 1 campeonato
    7 - Listar artilheiro em ordem de nome
    8 - Sair
    ''')
    opt = int(input('Digite a opção desejada: '))
    if opt == 1:
        incluir_gauchao()
    elif opt == 2:
        incluir_brasileirao()
    elif opt == 3:
        listar_artilheiros()
    elif opt == 4:
        artilheiros_campeonatos()
    elif opt == 5:
        artilheiros_gauchao()
    elif opt == 6:
        artilheiros_um_campeonato()
    elif opt == 7:
        listar_artilheiros_ordem()
    else:
        break