"""
Sorted

- Não é a mesma coisa que a função sort() o mesmo só funciona em lista
- Podemos utilizar o sorted() com qualquer iterável
- Como o próprio nome diz, sorted() serve para ordenar.
- sorted() gera uma nova lista ordenada
- O sorted() sempre retorna uma lista com os elementos de um iterável
"""
# Exemplo 1
numeros = [6, 1, 8, 2, 10, 41, 40, 37, 27, 10]
print(numeros)

print(sorted(numeros))
print(sorted({6, 1, 8, 2, 10, 41, 40, 37, 27, 10}))
print(sorted((6, 1, 8, 2, 10, 41, 40, 37, 27, 10)))

# Convertendo
print(sorted(set(numeros)))

# Adicionando paramêtros ao sorted()

# Do maior para o menor
print(sorted(numeros, reverse=True))

# Exemplos mais complexos
usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizza"]},
    {"username": "Diego", "tweets": []},
    {"username": "José", "tweets": [], "core": "amarelo"},
    {"username": "Kelly", "tweets": ["Eu adoro bolas", "Eu adoro macarrão", "Eu adoro feijão"]},
    {"username": "Roberto", "tweets": ["Eu adoro bolos"], "core": "vermelho"},
    {"username": "Astolfo", "tweets": ["Eu adoro pizza"], "core": "rosa"},
]

print(usuarios)
# Ordenando pelo username - Ordem Aufabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))
print(sorted(usuarios, key=lambda usuario: usuario["username"], reverse=True))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"]), reverse=True))

# Último exemplo
musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 4},
    {'titulo': 'Too old to rock''rol, too young to die', 'tocou': 32},
]

# Ordernar da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordernar da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
