from titulo import titulo


#====================================Programa Principal================================================
#carregar_goleadores()
while True:
	titulo("Seccão de Filmes", "*")
	print("1. Listar Filmes em Pelotas")
	print("2. Listar Filmes em Porto Alegre")
	print("3. Listar Todos os Filmes")
	print("4. Filmes Exclusivos de cada Cidade")
	print("5. Finalizar")

	opcao = int(input("Opcao: "))
	match opcao:
		case 1:
			listar_pelotas()
		case 2:
			listar_porto_alegre()
		case 3:
			listar_todos()
		case 4:
			excluidos_cidades()
		case other:
			break