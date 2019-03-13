"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é em string
"""

# Entrada de dados
print("Qual é o seu nome ?")
nome = input()

# Entrada de recebimento de dados 'moderna'
nome = input("Qual é o seu nome ? ")

# Exemplo de print 'antigo'
print("Seja bem vindo(a) %s" % nome)

# Exemplo de print 'morderno'
print("Seja bem vindo(a) {0}".format(nome))

# Exemplo de print 'mais atual' 3.7
print(f"Seja bem vindo(a) {nome}")

# Exemplo de recebimento de dados 'moderna'
print("Qual é a sua idade? ")
idade = input()

idade = int(input("Qual é a sua idade ? "))

# Processamento

# Saída de dados
# Exemplo de print 'antigo'
print("A %s tem %s anos" % (nome, idade))

# Exemplo de print 'moderno'
print("A {0} tem {1} anos".format(nome, idade))

# Exemplo de print 'mais moderno'
print(f"A {nome} tem {idade} anos")

"""
int(idade) é um cast
"""

print(f"A {nome} nasceu em {2018 - int(idade)}")
