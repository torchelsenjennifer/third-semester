import os
from statistics import fmean

alunos = []
idades = []
cursos = []


# arq = open("exercicioUm.txt", mode="r", encoding="utf-8")
# linhas = arq.readlines()

# # for linha in linhas:
#     alunos.append(linha.replace('\n', '').split(";"))

# print(alunos, end='')


# ===================================================================================

def ler_arquivo():
    #se o arquivo nao existe, retorna
    if not os.path.isfile("alunos.txt"):
        return

    #abre o arquivo para leitura
    with open("alunos.txt", "r") as arq:
        linhas = arq.readlines()

        for linha in linhas:
            #separa a linha em elementos de vetor, a cada ";"
            partes = linha.split(";")
            alunos.append(partes[0])
            idades.append(int(partes[1]))
            cursos.append(partes[2][0:-1])
        
        # print(alunos)
        # print(idades)
        # print(cursos)



def salva_arquivo():
    #abre o arquivo para gravação(sobrepoe o arquivo)
    with open("alunos.txt","w") as arq:
        for nome, idade, curso in zip(alunos, idades, cursos):
            arq.write(f"{nome};{idade};{curso}\n")

def titulo(texto, sublinhado="-"):
    print()
    print(texto)
    print(sublinhado*30)


def cadastrar():
    titulo("Inclusao de Alunos")
    nome = input("Nome do Aluno: ")
    idade = int(input("Idade do Aluno: "))
    curso = input("Curso: ")
    alunos.append(nome)
    idades.append(idade)
    cursos.append(curso)
    print("Ok! Aluno cadastrato com sucesso!")

def listar():
    titulo("Lista de Alunos Cadastrados")
    print("     |Nome do Aluno......|  |Idade.......|   |Curso......|")

    for x, (nome, idade, curso) in enumerate(zip(alunos, idades, cursos),start=1):
        print(f"{x:2}   |{nome:19}|  |{idade} anos     |   |{curso}       |")
       

def pesquisa():
    titulo("Pesquisa dos Alunos Cadastrados")
    pesq = input("Qual o nome do aluno a ser pesquisado: ")
    #se o nome pesquisado foi encontrado apresentar o cabeçalho uma vez
    # se o nome pesquisado foi encontrado apresentar nome
    # se nao encontrar apresentar mesagem
    # totalPesquisa = 0
    # encontradoNome = [] 
    # encontradoIdade = []
    # encontradoCurso = []

    # for x, (nome, idade, curso) in enumerate(zip(alunos, idades, cursos),start=1):
    #     if nome.lower() == pesq.lower():
    #         encontradoNome.append(nome)
    #         encontradoIdade.append(idade)
    #         encontradoCurso.append(curso)
    #         totalPesquisa =len(encontradoNome)

    # if(totalPesquisa>0):
    #     print("     |Nome do Aluno......|  |Idade.......|   |Curso......|")
    #     for x, (nome, idade, curso) in enumerate(zip(encontradoNome, encontradoIdade, encontradoCurso),start=1):
    #         print(f"{x:2}   |{nome:19}|  |{idade} anos     |   |{curso}       |")
    # else:
    #     print()
    #     print("Não foi encontrado!!")
    #     print()
    encontrado = False
    for x, (nome, idade, curso) in enumerate(zip(alunos, idades, cursos),start=1):
        if nome.lower() == pesq.lower():
            if encontrado == False:
                print("     |Nome do Aluno......|  |Idade.......|   |Curso......|")
                encontrado = True
            print(f"{x:2}   |{nome:19}|  |{idade} anos     |   |{curso}       |")

    if encontrado == False:
         print()
         print("Não foi encontrado!!")
         print()



def excluir():
    titulo("Exclusão de Alunos Cadastrados")
    print()
    listar()
    print()
    numeroAluno = int(input("Qual numero do aluno dejesa excluir: ")) 
    quantidadeAlunos = len(alunos)
    if numeroAluno >= quantidadeAlunos:
        print()
        print("INFORME UM NUMERO DE ALUNO VALIDO!")
        return
    else:
        exclusao = numeroAluno - 1
        del alunos[exclusao], idades[exclusao], cursos[exclusao]
        print()
        print('ALUNO EXCLUIDO COM SUCESSO!')
    

def resumo():
    quantidadeAlunos = len(alunos)
    media = fmean(idades)
    print(f'Quantidade de alunos: {quantidadeAlunos}')
    print(f'Media de idade: {media}')

def finalizar():
    salva_arquivo()

#ao iniciar o programa, carrega os dados salvos no arquivo
ler_arquivo()

while (True):
    print()
    titulo("Cadastro de Alunos", "-")
    print()

    print("-"*30)
    print("1. Cadastrar Aluno")
    print("2. Listar Aluno")
    print("3. Pesquisar por Nome")
    print("4. Excluir")
    print("5. Resumo(Nº de alunos e Média de idade)")
    print("6. Finalizar")

    opcao = int(input("Opção: "))

    if opcao == 1:
        cadastrar()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        pesquisa()
    elif opcao == 4:
        excluir()
    elif opcao == 5:
        resumo()
    elif opcao == 6:
        finalizar()
        break
    else:
        break
