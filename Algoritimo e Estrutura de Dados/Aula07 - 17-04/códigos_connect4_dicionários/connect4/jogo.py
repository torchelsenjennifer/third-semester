# declara constantes com o número de linhas e colunas
NUM_LINHAS = 6
NUM_COLUNAS = 7

# declara a matriz (vetor) do jogo
jogo = []

# função que cria a matriz do jogo, com o número de linhas e colunas
# sendo preenchido com " " (espaços), que indica posição disponível
def cria_jogo():
  for i in range(NUM_LINHAS): 
    jogo.append([])         # adiciona uma lista em cada linha do jogo
    for _ in range(NUM_COLUNAS):
      jogo[i].append(" ")   # adiciona um espaço " "

# mostra a matriz com as posições preenchidas
def mostra_jogo():
  print()
  for i, linha in enumerate(jogo, start=1):
    print(f"{i} |", end="")
    for casa in linha:
      print(f" {casa} ", end="")
    print("|")
  print("  +---------------------+")
  print("    1  2  3  4  5  6  7")

def linha_disponivel(coluna):
  disponivel = -1
  for i in range(NUM_LINHAS-1, -1, -1):
    if jogo[i][coluna] == " ":
      disponivel = i
      break
  return disponivel

def vencedor(simbolo):
  # quatro colunas consecutivas com o símbolo
  for l in range(NUM_LINHAS):
    for c in range(NUM_COLUNAS-3):
      if jogo[l][c] == simbolo and jogo[l][c+1] == simbolo and jogo[l][c+2] == simbolo and jogo[l][c+3] == simbolo:
        return True

  # quatro linhas consecutivas com o símbolo
  for l in range(NUM_LINHAS-3):
    for c in range(NUM_COLUNAS):
      if jogo[l][c] == simbolo and jogo[l+1][c] == simbolo and jogo[l+2][c] == simbolo and jogo[l+3][c] == simbolo:
        return True

  # quatro posições consecutivas na vertical (de cima para baixo, esquerda para direita)
  for l in range(NUM_LINHAS-3):
    for c in range(NUM_COLUNAS-3):
      if jogo[l][c] == simbolo and jogo[l+1][c+1] == simbolo and jogo[l+2][c+2] == simbolo and jogo[l+3][c+3] == simbolo:
        return True

  # quatro posições consecutivas na vertical (de cima para baixo, esquerda para direita)
  for l in range(NUM_LINHAS-1, NUM_LINHAS-3, -1):
    for c in range(NUM_COLUNAS-3):
      if jogo[l][c] == simbolo and jogo[l-1][c+1] == simbolo and jogo[l-2][c+2] == simbolo and jogo[l-3][c+3] == simbolo:
        return True

# chama as funções iniciais do programa
cria_jogo()
mostra_jogo()    

print("\nJogo Connect 4")
print("="*40)
print("Informe o número da coluna (1..7) ou 0 para sair")

# contador é usado para definir o jogador "x" ou "o" e 
# também o número de jogadas (para indicar empate)
contador = 1      

while True:
  # operador ternário do python
  jogador = "x" if contador % 2 == 1 else "o"

  coluna = int(input(f"\nJogador '{jogador}', informe a coluna: "))

  if coluna == 0 or coluna > NUM_COLUNAS:
    break

  linha = linha_disponivel(coluna-1)
  if linha == -1:
    print("Não há linhas disponíveis nesta coluna. Jogue novamente")
  else:
    jogo[linha][coluna-1] = jogador
    contador += 1

  mostra_jogo()

  if vencedor(jogador):
    print()
    print("*"*40)
    print(f"Parabéns Jogador '{jogador}'. Você é o vencedor!")
    print("*"*40)
    break

  if contador == NUM_COLUNAS*NUM_LINHAS:
    print()
    print("*"*40)
    print(f"Ah... Deu Empate")
    print("*"*40)
    break
