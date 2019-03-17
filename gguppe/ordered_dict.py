"""
Módulo Collections: Ordered Dict

https://docs.python.org/3/library/collections.html#collections.OrderedDict

- É um dicionário que garante a ordem de inserção dos elementos
"""

# Fazendo import
from collections import OrderedDict

# Em um dict a ordem de inserção não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'Chave = {chave} Valor = {valor}')

print()

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'Chave = {chave} Valor = {valor}')

print()

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionários comuns
# True -> Já que a ordem dos elementos não importam
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)

# Dicionários ordenados
# False -> Já que a ordem dos elementos importam
dict1 = OrderedDict({'a': 1, 'b': 2})
dict2 = OrderedDict({'b': 2, 'a': 1})

print(dict1 == dict2)
