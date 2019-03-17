"""
Módulo Collections - Named Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

- São tuple diferencia, onde especificamos um nome para a mesma e paramêtros
"""

# Fazendo import
from collections import namedtuple

# Recap Tuple
tupla = (1, 2, 3)
print(tupla)

# Precisamos definir o nome e params

# Forma 1
cachorro = namedtuple('cachorro', 'idade raça nome')

# Forma 2
cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Forma 3 - Mais recomendado
cachorro = namedtuple('cachorr', ['idade', 'raça', 'nome'])

# Usando
ray = cachorro(idade=2, raça='Chow-Chow', nome='Ray')

print(ray)
print(type(ray))

# Acessando

# Forma 1
print(ray[0])
print(ray[1])
print(ray[2])

print()

# Forma 2
print(ray.nome)
print(ray.idade)
print(ray.raça)

print()

# Outros métodos
print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))
