"""
Dicionários

OBS: Em algumas linguagens são conhecidos como mapas

Dicionários são coleções de chave e valor

Representados por {}

- A chave ou o valor podem ser de qualquer tipo de dado
- A forma de adicionar e atualizar são a mesmas
- Em dicionários não podemos ter chaves repetidas
- Também temos o Shallow Copy e Deep Copy
"""

print(type({}))

# Forma 1 mais comum
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 menos comum
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 acessando via chave da mesma forma que list/tuple
# OBS caso tentamos fazer um acesso com uma chave que não existe, será lançado um erro
print(paises['br'])
print(paises['py'])

# Forma 2 acessando via get - RECOMENDADA
# OBS caso o mesmo não esteja no dict, não será lançado um erro
# Igual ao 'TryGet' do C#
print(paises.get('br'))
print(paises.get('eua'))
print(paises.get('ru'))

pais = paises.get('ru')

if pais:
    print('Encontrei')
else:
    print('Não Encontrei')

# Define um valor padrão caso não seja encontrado
pais = paises.get('py', 'Não encontrado')
print(f'Pais encontrado ? {pais}')

# Se o valor está no dicionário
print('br' in paises)
print('eua' in paises)
print('ru' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean) inclusive list tuple como chaves
localidades = {
    (35.6896, 39.9787): 'Escritório em Tókio',
    (40.6476, 40.9777): 'Escritório em Nova Iorque',
    (37.6476, 37.9777): 'Escritório em São Paulo'
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário
print(paises)

# Forma 1 mais comum
paises['ru'] = 'Rússia'
print(paises)

# Forma 2 menos comum
paisNovo = {'ar': 'Argentina'}
paises.update(paisNovo)

print(paises)

# Atualizando dados em um dicionário

# Forma 1
paises['ar'] = 'Argentin'

print(paises)

# Forma 2
paises.update({'ar': 'Argentina'})

print(paises)

# Remover dados em um dicionários

print(paises)

# Forma 1 mais comum
# OBS: Precisamos sempre passar a chave, e caso não encontre um erro é lançado
# OBS: Ao removermos um valor do objeto o valor do mesmo é retornado.
paisRemovido = paises.pop('br')
print(paisRemovido)
print(paises)

# Forma 2
# OBS o valor removido não é retornado
del paises['ar']

print(paises)

# Imagine que voce tem um comércio eletrônico, onde temos um carrinho de compras no qual adicionamos produtos.
"""
Carrinho de Compras:
    Produto 1:
        - nome:
        - quantidade:
        - preço
    Produto 2:
        - nome:
        - quantidade:
        - preço

# Poderiams utilizar lista para isso ?
"""

# 1 - Poderiamos utilizar uma lista para isso ?
carrinho = []

produto1 = ['Playstation 4', 1, 1730.90]
produto2 = ['God of War 4', 1, 70.90]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teriamos que saber qual é o indice de cada informação do produto

# 2 Poderiamos utilizar uma tuple para isso ?
produto1 = ('Playstation 4', 1, 1730.90)
produto2 = ('God of War 4', 1, 70.90)

carrinho = (produto1, produto2)

print(carrinho)

# 3 Poderiamos utilizar um dicionário para isso ?
# Desta forma adicionamos ou removemos produto no carrinho e em cada produto podemos ter a certeza de cada informação
carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 1730.90}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preço': 70.90}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Métodos de dicionários
d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionário
d2 = d.copy()
d2['d'] = 45
d2.clear()

print(d2)

# Forma não usual de criação de dict
# O métodos fromkeys recebe dois paramêtros, um iterável e um valor
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuarios = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecidos')
print(usuarios)

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
