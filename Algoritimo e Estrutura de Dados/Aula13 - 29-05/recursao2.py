# recebe um numero e exibe cada numero (parte) em uma linha
def vertical(num):
    if num < 10:        # caso base
        print(num)
    else:
        vertical(num // 10) # 315, 31, 3
         # "//"" divisão de inteiros
		 # PILHA DE FUNÇÕES
        print(num % 10) #

vertical(3158)
