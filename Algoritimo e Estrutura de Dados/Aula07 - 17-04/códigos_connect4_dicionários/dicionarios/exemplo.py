# listas
nomes = []

# tuplas (é uma lista imutável)
bairros = ()

# dicionários
alunos = {}
alunos2 = dict()

# exemplo
contatos = {"Adriana": "99101.0203",
            "Bianca": "99988.7766",
            "Carlos": "98432.3232",
            "Débora": "99101.2030"}

# alterar o dicionário
contatos.update({"Eduardo": "99240.5566"})
contatos["Fernanda"] = "98114.1516"

#print(contatos)
#print(contatos["Bianca"])

# Percorrer os dicionários
## Retorna as chaves do dicionário
for nome in contatos.keys():
    print(nome)

## Retorna os valores do dicionário
for fone in contatos.values():
    print(fone)

## Retorna as chaves e valores do dicionário
for (nome, fone) in contatos.items():
    print(f"{nome} - Fone: {fone}")

print("=" * 40)
# Exemplo de utilização dos dicionários
## Criar uma lista de dicionários
clientes = [{"nome": "Fernando Souza", "idade": 24},
            {"nome": "Zilmar Costa", "idade": 21},
            {"nome": "Adriana Santos", "idade": 32},
            {"nome": "Carlos Nóbre", "idade": 28},
            {"nome": "Pedro Roberto", "idade": 19}]

print("Lista dos Clientes Cadastrados")
for cliente in clientes:
    print(f"{cliente['nome']} - {cliente['idade']} anos")
print()

# classificar a lista de dicionários
# lambda: define uma função anônima no Python
clientes2 = sorted(clientes, key=lambda cliente: cliente['nome'])

print("Lista dos Clientes em Ordem de Nome")
for cliente in clientes2:
    print(f"{cliente['nome']} - {cliente['idade']} anos")
print()

# por ordem de idade
clientes3 = sorted(clientes, key=lambda cliente: cliente['idade'])

print("Lista dos Clientes em Ordem de Idade")
for cliente in clientes3:
    print(f"{cliente['nome']} - {cliente['idade']} anos")
print()
