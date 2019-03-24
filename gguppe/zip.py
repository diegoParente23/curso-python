"""
Zip

zip() -> cria um iterável chamado (Zip Object) que agrega elemento de cada um dos iteráveis passados como entrada em
pares
"""
lista1 = [1, 2, 3, 8]
lista2 = [4, 5, 6, 7]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma list, tuple e dict
zipConvertido = list(zip1)
print(list(zipConvertido))
print(tuple(zipConvertido))
print(set(zipConvertido))
print(dict(zipConvertido))

lista3 = [7, 8, 9, 10, 11]

# OBS: O zip utiliza como paramêtro o menor tamanho como iterável, significa que se tiver trabalhando com
# iteráveis com tamanhos distintos irá parar quando os elementos do menor iterável acabar.
zip2 = zip(lista1, lista2, lista3)
print(list(zip2))

# Podemos utilizar diferentes iteráveis com zip
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

zip3 = zip(tupla, lista, dicionario.values())
print(list(zip3))

# Lista de tuplas
dados = [(0, 1), (1, 2), (2, 3), (3, 4)]
print(list(zip(*dados)))

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['mario', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(dict(final))

# Podemos utilizar o map
final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))
