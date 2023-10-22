
import os

instrumentos = []
marcas = []
precos = []

def ler_arquivo():
    if not os.path.isfile("instrumentos.txt"):
        return
    
    with open("instrumentos.txt", "r") as arq:
        linhas = arq.readlines()

        for linha in linhas:
            partes = linha.split(";")
            instrumentos.append(partes[0])
            marcas.append(partes[1])
            precos.append(float(partes[2][0:-1]))

def salva_arquivo():
    with open("instrumentos.txt","w") as arq:
        for instrumento, marca, preco in zip(instrumentos, marcas, precos):
            arq.write(f"{instrumento};{marca};{preco}\n")

def titulo(texto):
    print()
    print(texto)

def incluir():
    print("")
    titulo("INCLUSÃO DE INSTRUMENTOS")
    print("")
    instrumento = input("Qual o nome do Instrumento: ")
    marca = input("Qual a marca do Instrumento: ")
    preco = float(input("Qual o preço do Instrumento R$: "))
    instrumentos.append(instrumento)
    marcas.append(marca)
    precos.append(preco)
    print("")
    print("Ok!INSTRUMENTO CADASTRADO COM SUCESSO")

def listar():
    titulo("Lista dos Instrumentos Cadastrados")
    print("    |Nome do Instrumento......|  |Marca.......|   |Preço R$......|")

    for x, (instrumento, marca, preco) in enumerate(zip(instrumentos, marcas, precos),start=1):
        print(f"{x:1}   |{instrumento:25}|  |{marca:6}      |   |{preco:7.2f}       |")
    
def pesquisa():
        titulo("Pesquisa pela Marca do Instrumento")
        pesq = input("Qual a marca do Instrumento desejado: ")
        encontrado = False
        for x, (instrumento, marca, preco) in enumerate(zip(instrumentos, marcas, precos),start=1):
            if marca.lower() == pesq.lower():
                if encontrado == False:
                    print("    |Nome do Instrumento......|  |Marca.......|   |Preço R$......|")
                    encontrado = True
                print(f"{x:1}   |{instrumento:25}|  |{marca:6}      |   |{preco:7.2f}       |")

        if encontrado == False:
         print()
         print("Não foi encontrado nenhuma MARCA!!")
         print()

def excluir():
        titulo("Exclusão de Instrumento Músical")
        print()
        listar()
        print()
        numeroInstrumento = int(input("Qual o número do Instrumento Músical deseja excluir: ")) 
        quantidadeInstruemtnos = len(instrumentos)
        if numeroInstrumento >= quantidadeInstruemtnos:
            print()
            print("INFORME UM NUMERO DE REFERENCIA VÁLIDO!")
            return
        else:
            exclusao = numeroInstrumento - 1
            del instrumentos[exclusao], marcas[exclusao], precos[exclusao]
            print()
            print('INSTRUMENTO MÚSICAL EXCLUIDO COM SUCESSO!')

# 5. Pesquisa com totalização (por instrumento: mostrar número e preço total
# do instrumento pesquisado; número e preço total dos outros instrumentos)

def pesquisaTotalizacao():
        pesqNome = input("Qual o nome do Instrumento a ser pesquisado: ")
        encontrado = False
        pesqTotal = 0
        valorTotal = 0
        outrosInst = 0
        saldoTotal = 0
        for x, (instrumento, marca, preco) in enumerate(zip(instrumentos, marcas, precos),start=1):
            if pesqNome.lower() == instrumento.lower():
                 if encontrado == False:
                    pesqTotal = pesqTotal + 1
                    valorTotal = valorTotal + preco
                    encontrado = True
            else:
                outrosInst = outrosInst + 1
                saldoTotal = saldoTotal + preco
        print("")
        print("="*50)
        print(f'Quantidade de {pesqNome}: {pesqTotal}')
        print(f'Preco total do Instrumento {pesqNome}: R${valorTotal}')
        print("="*50)
        print("")
        print("="*50)
        print(f"Quantidade de intrumentos restantes: {outrosInst}")
        print(f"Valor total em reias dos intrumentos restantes: R${saldoTotal:6.2f}")
        print("="*50)
        if encontrado == False:
            print()
            print("Não foi encontrado nenhum INSTRUMENTO!!")
            print()

ler_arquivo()

while (True):
    print()
    titulo("Cadastro de Instrumentos Músicais")
    print()

    print("1. Incluir Instrumento")
    print("2. Listar Instrumento")
    print("3. Pesquisar por Marca do Instrumento")
    print("4. Excluir Instrumento Musical (por numero)")
    print("5. Pesquisa com Totalização")
    print("")
    opcao = int(input("Digite a opção buscada: "))

    if opcao == 1:
        incluir()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        pesquisa()
    elif opcao == 4:
        excluir()
    elif opcao == 5:
        pesquisaTotalizacao()
    else:
        salva_arquivo()
        break