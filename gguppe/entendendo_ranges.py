"""
Entendendo ranges

Ranges são utilizados para gerar sequencias numéricas,
não de formas aleatórias e sim de maneira especifica

Formas gerais

1.

range(valor_de_parada)

OBS: valor_de_parada não inclusive (iniciado por padrão 0, e passo de 1 em 1)

2.

range(valor_de_inicio, valor_de_parada)

3.

range(valor_de_inicio, valor_de_parada, passo)

4. Inversa

range(valor_de_inicio, valor_de_parada, passo)
"""
# 1.
for num in range(11):
    print(num)

# 2.
for num in range(1, 11):
    print(num)

# 3.
for num in range(0, 50, 5):
    print(num)

# 4.
for num in range(10, -1, -1):
    print(num)
