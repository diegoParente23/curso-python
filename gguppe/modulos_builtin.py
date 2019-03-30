"""
Módulos Buil-in (Módulos integrados que já vem instalados no Python)
_________________________
|Python|Módulos built-in|
-------------------------

# Utilizando alias (apelidos) para módulos e funções
# OBS a partir daqui a palavra 'random' não funcionára mais somente o alias
import random as rdm

print(rdm.shuffle())

# Podemos importar todas as funções de um módulos utilizando o *
# OBS o comando abaixo é diferente do de cima, embora ambos importem todos as funções, no comando abaixo
# não precisamos utilizar o nome do módulo.função ex: random() ou shuffle()
from random import *

numeros = [1, 2, 3, 4, 5]
shuffle(numeros)
print(numeros)

# Importando o módulo completo
import random

print(random.random())

# Utilizando o alias para funções
from random import randint as rdi

print(rdi(6, 95))

# Importando mais funções com alias
from random import randint as rdi, random as rdm

print(rdi(1, 100))
print(rdm())

# Importe confuso
from random import random, randint, shuffle, choice
"""
# Costumamos utilizar tuple para colocar multiplos imports de um mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())
print(randint(1, 50))
print(choice('University'))
lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)
