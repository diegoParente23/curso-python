"""
Reversed

OBS: Não confunda com a função reserve() que utilizamos nas listas
    - A função reverse() só funciona em listas
    - A função reversed() funciona em qualquer iterável
    - Sua função é inverter o iterável
    - A função retornar um iterável chamado de List Reverse Iterator
"""
# Exemplos
lista = [1, 2, 3, 4, 5]
print(lista)

res = reversed(lista)
print(res)
print(type(res))

# Podemos converter o elemento para uma List, Tuple ou Set

# list
print(list(reversed(lista)))

# tuple
print(tuple(reversed(lista)))

# set
# Em conjuntos não definimos a ordem dos elementos
print(set(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed('Geek University'):
    print(letra, end='')

print()

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))

# Com slice string
print('Geek University'[::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverse
for n in reversed(range(0, 10)):
    print(n)

print()

# Podemos também fazer isso utilizando o próprio range()
for n in range(9, -1, -1):
    print(n)
