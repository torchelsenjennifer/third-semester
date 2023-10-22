nome_arq = input("Nome do Arquivo: ")
# abre o arquivo para leitura
arq = open(nome_arq, mode="r", encoding="utf-8")

# insere cada palavra do texto (convertida em maiúscula)
# em um vetor - usa o split() para separar as palavras
palavras = []
for linha in arq:
    for palavra in linha.split():
        if len(palavra) >= 3:
            palavras.append(palavra.upper())

# print(palavras)
dicionario = {}
for palavra in palavras:
    # busca a chave no dicionário e retorna None
    # se não existir
    num = dicionario.get(palavra, None)

    # se não existir a chave
    if num == None:
        # acrescenta uma chave no dicionario com valor 1
        dicionario[palavra] = 1
    else:
        # se já existe, adiciona 1
        dicionario[palavra] = num + 1

#print(dicionario)
# obtém o maior valor da lista
maior = max(dicionario.values())
# apresenta qual a palavra tem esse valor
for chave in dicionario:
    if dicionario[chave] == maior:
        print(f"Palavra: {chave} - {maior} ocorrências")
        break

# ordena o dicionário em ordem inversa de ocorrências
destaques = sorted(dicionario.items(), 
                   key=lambda d : d[1], reverse=True)

for i, (palavra, num) in enumerate(destaques, start=1):
    print(f"{i}ª: {palavra} - {num} x")
    if i == 20:
        break