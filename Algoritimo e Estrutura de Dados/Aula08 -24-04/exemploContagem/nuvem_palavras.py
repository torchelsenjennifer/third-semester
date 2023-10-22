nome_arq = input("Nome do arquivo: ")
#abre o arquivo para leitura
arq = open(nome_arq, "r", encoding="utf-8")

#insere cada palavra do texto (convertida em maiuscula)
#em um vetor - usa o split() para separar as palavras

palavras =[]

for linha in arq:
    for palavra in linha.split():
	    if len(palavra)>=3:
		    palavras.append(palavra.upper())

#print(palavras)
dicionario = {}
for palavra in palavras:
        # busca a chave no dicionario e retorna None
		# se nao existir a chave
		num = dicionario.get(palavra, None)
		if num == None:
			#acrescenta uma chave no dicionario com valor 1
			dicionario[palavra] = 1
		else:
			#se ja existi, adiciona
			dicionario[palavra] = num + 1

#print(dicionario)
#obtem o maior valor da lista
maior = max(dicionario.values())
#apresenta qual a palavra tem esse valor
for chave in dicionario:
	if dicionario[chave]  == maior:
		print(f"Palavra: {chave} - {maior} ocorrencias")
		break

#ordena o dicionario em ordem inversa de ocorrencias
destaques = sorted(dicionario.items(), key=lambda d : d[1], reverse=True)

for i, (palavra, num) in enumerate(destaques, start=1):
	print(f"{i}ª: {palavra} - {num} x")
	if i == 20:
		break