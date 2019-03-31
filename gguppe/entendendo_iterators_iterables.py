"""
Entendendo Iterators e Iterables

- Iterator
    -> Um objeto que pode ser iterado.
    -> Um objeto que retorna um dado. sendo um elemento por vez quando uma função next() é chamada.

- Iterable
    -> Um objeto que irá retornar um iterator quando a função iter() for chamada.
"""

# É um iterable porém não é um iterator
nome = 'Geek University'
numeros = [1, 2, 3, 4, 5]

print(nome)
print(numeros)

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print()

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
