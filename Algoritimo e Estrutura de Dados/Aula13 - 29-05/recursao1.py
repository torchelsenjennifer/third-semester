# exemplo de funcao recursiva
# (chama a si mesma, dentro da funcao)

def contagem(num): #recebe num
    if num >5 : #se numero menor que entra no if
        print('Lanacar!!') #printa a informa�ao
    else: # se nao cai aqui
        contagem(num+1)# chama a funcao novamente e passa o numero menos 1
        print(num) #printa so o numero
		#PILHA
contagem(1)

# #funcao equivalente, sem recursao
# def contagem2(num): #recebe num
#     for i in range(num, -1, -1): #faz num de vezes e vai printando
#         print(i)
#     print('Lancar!!')

# contagem2(5)