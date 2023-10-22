import os

# declara os vetores globais
nomes = []
apostas = []
valores = []

def obter_dados_do_arquivo():
  # se o arquivo não existe, retorna
  if not os.path.isfile("apostas.txt"):
    return
  
  # abre o arquivo para leitura
  with open("apostas.txt", "r") as arq:
    # lê todas as linhas do arquivo (carregando em um vetor)
    linhas = arq.readlines()

    for linha in linhas:
      # separa a linha em elementos de vetor, a cada ";"
      partes = linha.split(";")
      nomes.append(partes[0])
      apostas.append(partes[1])
      valores.append(float(partes[2][0:-1]))    

def salvar_dados_no_arquivo():
  # abre o arquivo para gravação (sobrepõe os dados)
  with open("apostas.txt", "w") as arq:
    
    for nome, aposta, valor in zip(nomes, apostas, valores):
      arq.write(f"{nome};{aposta};{valor}\n")

def titulo(texto, sublinhado="-"):
  print()
  print(texto)
  print(sublinhado*30)

def incluir():
  titulo("Inclusão de Aposta: Caxias x Grêmio")
  nome = input("Nome do Apostador: ")
  
  while True:
    # lê a entrada e já converte para minúsculas
    aposta = input("Aposta (formato 2x1): ").lower()

    partes = aposta.split("x")
    if len(partes) != 2:
      print("Formato incorreto")
      continue                    # volta ao início do laço

    # strip: retira os espaços da string
    if not partes[0].strip().isdigit() or not partes[1].strip().isdigit():
      print("Informe somente números no placar") 
      continue                    # volta ao início do laço

    break

  valor = float(input("Valor da Aposta R$: "))

  # acrescenta aos vetores os dados recebidos
  nomes.append(nome)
  apostas.append(aposta)
  valores.append(valor)

def listar():
  titulo("Listagem das Apostas - Caxias x Grêmio")

  print("Nome do Apostador.............  Aposta:  Valor R$:")

  for nome, aposta, valor in zip(nomes, apostas, valores):
    print(f"{nome:30}  {aposta:^7}  {valor:9.2f}")

def listar_resultados():
  titulo("Listagem das Apostas - Caxias x Grêmio")

  print("Nome do Apostador.............  Aposta")

  for nome, aposta in zip(nomes, apostas):
    partes = aposta.split("x")
    if int(partes[0]) > int(partes[1]):
      apostou = "Caxias"
    elif int(partes[0]) == int(partes[1]):
      apostou = "Empate"
    else:
      apostou = "Grêmio"
    print(f"{nome:30}  {apostou}")
  
def totalizar():
  numero_aposta = len(nomes)
  total_dinheiro = sum(valores)
  print(f"Numero de apostas: {numero_aposta} ")
  print(f"Total de dinheiro apostado: {total_dinheiro:0.2f}")

def apostas_resultado():
  pass

def resultado():
  pass


# Ao iniciar o programa, ler os dados salvos no arquivo
obter_dados_do_arquivo()

while True:
  titulo("AvenidasBet–Controle de Apostas\nCaxias x Grêmio (Final do Gauchão 2023)", "=") 
  print("1. Cadastrar Aposta")
  print("2. Listar Apostas")
  print("3. Listar Resultado")
  print("4. Total de Apostas")
  print("5. Apostas por Resultado")
  print("6. Resultado e Premiação")
  print("7. Finalizar")
  opcao = int(input("Opção: "))
  if opcao == 1:
    incluir()
  elif opcao == 2:
    listar()
  elif opcao == 3:
    listar_resultados()
  elif opcao == 4:
    totalizar()
  elif opcao == 5:
    apostas_resultado()
  elif opcao == 6:
    resultado()
  else:
    # salva os dados dos vetores no arquivo
    salvar_dados_no_arquivo()
    break