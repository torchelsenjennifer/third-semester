import os

alunos = []
idades = []
cursos = []


def ler_arquivo():
    #se o arquivo nao existe, retorna
    if not os.path.isfile("alunos.txt"):
        return

    #abre o arquivo para leitura
    with open("alunos.txt", "r") as arq:
        linhas = arq.readlines()
        print(linhas)
        # for linha in linhas:
        #     #separa a linha em elementos de vetor, a cada ";"
        #     partes = linha.split(";")
        #     alunos.append(partes[0])
        #     idades.append(int(partes[1]))
        #     cursos.append(partes[2][0:-1])

ler_arquivo()