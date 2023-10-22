import csv
titanic = []

def carrega_dados():
	with open('titanic.csv', mode='r', encoding="utf-8") as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for linha in csv_reader:
			titanic.append(linha)

def titulo(msg, traco='-'):
    print()
    print(msg)
    print(traco*40)

def dados_gerais():
	titulo("Dados Gerais dos Passageiros")
	num = len(titanic)
	sobreviventes = 0
	mortos = 0
	masculino = 0
	feminino = 0
	classeA = 0
	classeB = 0
	classeC = 0
#  verificar for dms
	for passageiro in titanic:
		if passageiro["Survived"] == "1":
			sobreviventes += 1
		else:
			mortos += 1
	for passageiro in titanic:
		if passageiro["Sex"] == "female":
			feminino += 1
		if passageiro["Sex"] == "male":
			masculino += 1
	for passageiro in titanic:
		if passageiro["Pclass"] == "1":
			classeA += 1
		if passageiro["Pclass"] == "2":
			classeB += 1
		if passageiro["Pclass"] == "3":
			classeC += 1

	print(f'Numero de Passageiros: {num}')
	print(f'Numero de Sobreviventes: {sobreviventes}')
	print(f'Numero de Mortos: {mortos}')
	print(f'Mulheres: {feminino}')
	print(f'Homens: {masculino}')
	print(f'CLASSE A: {classeA}')
	print(f'CLASSE B: {classeB}')
	print(f'CLASSE C: {classeC}')

def sobreviventesSexo():
	titulo("Sobreviventes do sexo Masculino e Feminino")
	mulherViva = 0
	mulherMorta = 0
	homemMorto = 0
	homemVivo = 0
	for passageiro in titanic:
		if  passageiro["Survived"] == "1" and passageiro["Sex"] == "female":
			mulherViva += 1
		if passageiro["Survived"] == "0" and passageiro["Sex"] == "female":
			mulherMorta += 1
		if passageiro["Survived"] == "1" and passageiro["Sex"] == "male":
			homemVivo += 1
		if passageiro["Survived"] == "0" and passageiro["Sex"] == "male":
			homemMorto += 1
	print(f'Mulheres: Sobreviventes: {mulherViva} Mortas: {mulherMorta}')
	print(f'Homens: Sobreviventes: {homemVivo} Mortos: {homemMorto}')

def sobrevivente_classe():
	titulo("Sobreviventes por Por CLASSE")
	femininoVivoA = 0
	femininoMortoA = 0
	masculinoVivoA = 0
	masculinoMortoA = 0
	femininoVivoB = 0
	femininoMortoB = 0
	masculinoVivoB = 0
	masculinoMortoB = 0
	femininoVivoC = 0
	femininoMortoC = 0
	masculinoVivoC = 0
	masculinoMortoC = 0
	for passageiro in titanic:
		if passageiro["Pclass"] == "1" and passageiro["Survived"] == "1" and passageiro["Sex"] == "female":
			femininoVivoA += 1
		if passageiro["Pclass"] == "1" and passageiro["Survived"] == "0" and passageiro["Sex"] == "female":
			femininoMortoA += 1
		if passageiro["Pclass"] == "1" and passageiro["Survived"] == "1" and passageiro["Sex"] == "male":
			masculinoVivoA += 1
		if passageiro["Pclass"] == "1" and passageiro["Survived"] == "0" and passageiro["Sex"] == "male":
			masculinoMortoA += 1
		if passageiro["Pclass"] == "2" and passageiro["Survived"] == "1" and passageiro["Sex"] == "female":
			femininoVivoB += 1
		if passageiro["Pclass"] == "2" and passageiro["Survived"] == "0" and passageiro["Sex"] == "female":
			femininoMortoB += 1
		if passageiro["Pclass"] == "2" and passageiro["Survived"] == "1" and passageiro["Sex"] == "male":
			masculinoVivoB += 1
		if passageiro["Pclass"] == "2" and passageiro["Survived"] == "0" and passageiro["Sex"] == "male":
			masculinoMortoB += 1
		if passageiro["Pclass"] == "3" and passageiro["Survived"] == "1" and passageiro["Sex"] == "female":
			femininoVivoC += 1
		if passageiro["Pclass"] == "3" and passageiro["Survived"] == "0" and passageiro["Sex"] == "female":
			femininoMortoC += 1
		if passageiro["Pclass"] == "3" and passageiro["Survived"] == "1" and passageiro["Sex"] == "male":
			masculinoVivoC += 1
		if passageiro["Pclass"] == "3" and passageiro["Survived"] == "0" and passageiro["Sex"] == "male":
			masculinoMortoC += 1
	print(f'Sobreviventes da CLASSE A: Mulheres: {femininoVivoA} Masculino: {masculinoVivoA}')
	print(f'Mortos da CLASSE A: Mulheres: {femininoMortoA} Masculino: {masculinoMortoA}')
	print(f'Sobreviventes da CLASSE B: Mulheres: {femininoVivoB} Masculino: {masculinoVivoB}')
	print(f'Mortos da CLASSE B: Mulheres: {femininoMortoB} Masculino: {masculinoMortoB}')
	print(f'Sobreviventes da CLASSE C: Mulheres: {femininoVivoC} Masculino: {masculinoVivoC}')
	print(f'Mortos da CLASSE C: Mulheres: {femininoMortoC} Masculino: {masculinoMortoC}')

def estatistica():
	titulo("Estatistica geral")

	titanic2 = titanic
	lista = sorted(numeros.items(), key=lambda, if else)

	print(lista[0])

carrega_dados()

while True:
	titulo('Estatistica dos Passageiros do Titanic', '-')
	print('1. Dados Gerais')
	print('2. Sobreviventes por Sexo')
	print('3. Sobrevivente por classe')
	print('4. Estatistica de Idade')
	print('5. Finalizar')
	opcao = int(input("opcao: "))

	if opcao == 1:
		dados_gerais()
	elif opcao == 2:
		sobreviventesSexo()
	elif opcao == 3:
		sobrevivente_classe()
	elif opcao == 4:
		estatistica()
	else:
		break