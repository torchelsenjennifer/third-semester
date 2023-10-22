

# dicionarios
alunos = {}
alunos2 = dict()

#exemplo
contatos = {"Adriana": "99101.0203",
            "Bianca": "99988.7766",
            "Carlos": "981052090",
            "Debora": "981214579"}

print(contatos)
print(contatos["Bianca"])

#alterar o dicionario
contatos.update({"Eduardo":"99240.5566"})
contatos["Fernanda"] = "98114.1516"

# print(contatos)
# print(contatos["Bianca"])

#percorrer os dicionarios
for nome in contatos.keys():
    print(nome)

#Retorna os valores do dicionario
for fone in contatos.values():
    print(fone)

#Retorna as chaves e valores do dicionario
for(nome, fone) in contatos.items():
    print(f"{nome} - Fone: {fone}")
print("="*20)
# Exemplo de utilização dos dicionarios
## Criar uma lista de dicionarios
clientes = [{"nome": "Fernando Souza","idade":24},
            {"nome": "Zilmar Costa","idade":21},
            {"nome": "Adriana Santos","idade":32},
            {"nome": "Carlos Nobre","idade":28},
            {"nome": "Pedro Roberto","idade":19},]

print('Lista dos Clientes Cadastrado')
for cliente in clientes:
    print(f"{cliente['nome']} - {cliente['idade']} anos")
print()

#classificar a lsita de dicionarios
#lambda: define uma função anonima no python

cliente2 = sorted(clientes, key=lambda cliente: cliente['nome'])
print('Lista dos Clientes em Ordem de Nome')
for cliente in cliente2:
    print(f"{cliente['nome']} - {cliente['idade']} anos")
print()

#por ordem de idade
cliente3 = sorted(clientes, key=lambda cliente: cliente['idade'])
print('Lista dos Clientes em Ordem de Idade')
for cliente in cliente2:
    print(f"{cliente['nome']} - {cliente['idade']} anos")
print()