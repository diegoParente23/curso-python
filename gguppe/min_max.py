"""
Min e Max

max() -> retorna o maior valor em um iterável ou maior de dois ou mais elementos
    - Podemos passar quantos valores quiser

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informa o primeiro valor: '))
val2 = int(input('Informa o segundo valor: '))

print(f'O maior valor é: {max(val1, val2)}')

- min() retorna o menor valor em um interável ou de dois ou mais elementos
"""
# Exemplo Max
lista = [1, 9, 4, 99, 34, 123]
print(max(lista))

tupla = (1, 9, 4, 99, 34, 123)
print(max(tupla))

conjunto = {1, 9, 4, 99, 34, 123}
print(max(conjunto))

dicionario = {'a': 1, 'b': 9, 'c': 4, 'd': 99, 'e': 34, 'f': 123}
# Maior pela chave
print(max(dicionario))
# Maior pelo valor
print(max(dicionario.values()))

# Entre dois valores
print(max(3, 43))

print(max(4, 64, 14, 97))
print(max('a', 'b', 'c'))
print(max('a', 'ab', 'abc'))
print(max(3.145, 5.798))
print(max('Geek University'))

print()
print()

# Exemplo Min
lista = [1, 9, 4, 99, 34, 123]
print(min(lista))

tupla = (1, 9, 4, 99, 34, 123)
print(min(tupla))

conjunto = {1, 9, 4, 99, 34, 123}
print(min(conjunto))

dicionario = {'a': 1, 'b': 9, 'c': 4, 'd': 99, 'e': 34, 'f': 123}
# Maior pela chave
print(min(dicionario))
# Maior pelo valor
print(min(dicionario.values()))

# Entre dois valores
print(min(3, 43))

print(min(4, 64, 14, 97))
print(min('a', 'b', 'c'))
print(min('a', 'ab', 'abc'))
print(min(3.145, 5.798))
# Neste caso o menor é o ' ' pois ele é o menor
print(min('Geek University'))

# Outros exemplos
# OBS Neste cenário ele pega em ordem aufabética
nomes = ['Arya', 'Samsin', 'Dora', 'Tim', 'Ollivander']
print(max(nomes))
print(min(nomes))

print()

# Passamos o lambda para alterar a forma como será realizado a função
# Olhando agora para o tamnho da string
print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 4},
    {'titulo': 'Too old to rock''rol, too young to die', 'tocou': 32},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

print()

# D E S A F I O !
# Imprima somente o titulo da musica mais e menos tocada
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

print()

# D E S A F I O !
# Como encontrar a musica mais tocada e a menos tocada sem usar max(), min() e lambda ?
max = 0
min = 999999
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])

print(max)
print(min)

