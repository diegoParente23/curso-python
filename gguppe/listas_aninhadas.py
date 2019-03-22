"""
Listas aninhadas (Nested List)

Algumas linguagens de programação possuem classe chamadas arrays, podendo ser
    - Unidimensional (Array/Vetores)
    - Multidimensional (Matriz)

Em python nós temos listas

numero = [1, 2, 3, 4, 5, 6]
"""
# Exemplos

# Matriz 3x3
listas = [[1, 2, 3], [6, 7, 8], [3, 4, 5]]
print(listas)

# Acessar os dados
print(listas[0])
print(listas[0][1])
print(listas[1][2])

# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)

print()

# List Comprehensions
[[print(valor) for valor in lista] for lista in listas]

# Outros exemplos
# Gerando um tabuleiro 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

# Gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
for linha in velha:
    print(linha)

# Gerando valores iniciais
print([['*' for i in range(1, 4)] for j in range(1, 4)])
