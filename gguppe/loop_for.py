"""
Estrutura de repetição

Loop for

Exemplos

for indice, letra in enumerate(name):
    print(name[indice])

for indice, letra in enumerate(name):
    print(letra)

OBS: Quando não precisamos de um valor podemos descarta-lo usando
o '_'
for _, letra in enumerate(name):
    print(letra)

OBS o enumerate retorna uma tupla <index, value>

for valor in enumerate(name):
    print(valor)

qtde = int(input('Quantas vezes o for deve interar ? '))
soma = 0

for n in range(1, qtde + 1):
    num = int(input(f'Informe o {n}/{qtde} valor: '))
    soma += num

print(f'A soma é {soma}')
"""

name = 'Diego Parente'
for item in name:
    print(item)

print(name[0:5])

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for item in numero:
    print(item)

"""
OBS: no range o valor final não é inclusive,
portanto irá imprimir do 1 ao 9
"""
lista = range(1, 10)
for item in lista:
    print(item)

for _, letra in enumerate(name):
    print(letra)

curso = 'Geek University'

for letra in curso:
    print(letra, end='')

curso *= 10

print(curso)

# Original U+1F60D
# Modificado U0001F60D -> trocar sinal de mais por '000'
for _ in range(3):
    for aux in range(1, 11):
        print('\U0001F60D' * aux)
