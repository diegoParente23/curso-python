"""
Any e All

- Pode ser usado em qualquer estrutura de lista desde que seja um iterável.

all() -> retorna true se todos os elementos do iterável são verdadeiros ou se ainda o iterável está vazio
any() -> retorna true se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio retorna false
"""
# All
# Todos os números são verdadeiros ?
# False
print(all([0, 1, 2, 3, 4, 5, 6, 7]))

# True
print(all([1, 2, 3, 4, 5, 6, 7]))

# Exemplo 2
nomes = ['Carlos', 'Camila', 'Carla', 'Catiana']

print(all([nome[0] == 'C' for nome in nomes]))

# Exemplo 3
# OBS: Um iterável vazio convertido em boolean é False mas o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))

# Exemplo 4
print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

numeros = [1, 7, 3, 5, 5, 9, 7]
print(all(filter(lambda num: num % 2 == 0, numeros)))

# Any
# Exemplo 1
print(any(filter(lambda num: num % 2 == 0, numeros)))

# Exemplo 2
print(any([nome[0] == 'C' for nome in nomes]))

# Exemplo 3
print(any([num for num in range(0, 50, 3) if num % 2 == 0]))
