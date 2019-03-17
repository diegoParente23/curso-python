"""
Mapas

São conhecidos em python como dicionários

Dicionários em python são representados por chaves {}
"""

receita = {'jan': 200, 'fev': 234, 'mar': 400}

# Iterar sobre dicionários
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave}: recebi R$ {receita[chave]}')

print(receita.keys())
print(receita.values())

# Modo Pythônico
for key in receita.keys():
    print(key)

# Modo Pythônico
for value in receita.values():
    print(value)

# Desempacotamento de dicionários
print(receita.items())

for chave, value in receita.items():
    print(f'chave={chave} e valor={value}')

# Soma*, Valor Máximo*, Valor Minimo*, Tamanhi
# * Se os valores forem inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
