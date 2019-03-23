"""
Filter

- filter() -> Serve para filtrar dados em uma coleção
- Assim como na função map, após serem utilizados os dados de filter(), eles serão apagados da memória.
- A diferença entre 'map' e 'filter'
    - Map -> Recebe dois paramêtros, uma função e um iterável e retorna um ojeto mapeando a função para cada elemento
    do iterável
    - Filter -> Recebe dois paramêtros, uma função e um iterável e retorna um valor filtrando apenas os elementos
    de acordo com a função
"""
# Lib para trabalhar com dados estatisticos
import statistics

# Exemplo 1
valores = 1, 2, 3, 4, 5, 6
media = (sum(valores) / len(valores))
print(media)

# Exemplo 2
dados = [1.2, 2.7, 8.4, 4.5, 3.8, 2.2, -1.2]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(media)

# OBS assim como a função map a filter recebe dois paramêtros, um sendo uma função e o outro o iterável
res = filter(lambda x: x > media, dados)
print(list(res))

res = filter(lambda x: x < media, dados)
print(type(res))
print(list(res))
print(f'Novamente {list(res)}')

paises = ['', 'Argentina', '', '', 'Brasil', 'Chile', 'Equador', 'Paraguai', '', '', '']
print(paises)

res = filter(None, paises)
print(list(res))

res = filter(lambda pais: len(pais) > 0, paises)
res = filter(lambda pais: pais != '', paises)
print(list(res))

# Exemplo mais complexo
usuarios = [
    {"uername": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizza"]},
    {"uername": "Diego", "tweets": []},
    {"uername": "José", "tweets": []},
    {"uername": "Kelly", "tweets": ["Eu adoro bolas", "Eu adoro macarrão", "Eu adoro feijão"]},
    {"uername": "Roberto", "tweets": ["Eu adoro bolos"]},
    {"uername": "Astolfo", "tweets": ["Eu adoro pizza"]},
]
print(usuarios)

# Filtrar os usuários que estão inativos no twitter

# Forma 1
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
ativos = list(filter(lambda usuario: len(usuario['tweets']) > 0, usuarios))
print(inativos)
print(ativos)

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

# Como combinar filter com map
# Devemos criar uma lista contendo 'Sua instrutora é + nome, desde que cada nome tenha menos de 5 caracteres
nomes = ['Vanessa', 'Ana', 'Maria']

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)

# Praticando
checkoutItems = [
    {'productId': 1, 'productName': 'SKOL', 'quantity': 10, 'unitPrice': 10.90},
    {'productId': 2, 'productName': 'STELA', 'quantity': 5, 'unitPrice': 12.90}
]
res = map(lambda checkout_item: checkout_item['quantity'] * checkout_item['unitPrice'], checkoutItems)
print(list(res))
