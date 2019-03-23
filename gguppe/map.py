"""
Map

Com map, fazemos mapeamento de valores para funções

OBS: Após utilizar a função map, na primeira utilização, o resultado zera.
"""
# Importação
import math


def area(r):
    """Cálcula á de um círculo com ráio 'r'"""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.9))

raios = [2, 4, 5, 1, 12, 56, 23, 19]

# Forma comum
areas = []
for r in raios:
    areas.append((area(r)))
print(areas)

# Forma 2 utilizando map
# Map é uma função que recebe 2 paramêtros: O primeiro a função, O segundo um iterável
print(areas)
areas = map(area, raios)
print(type(areas))

# Forma 3 com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# Para fixar

# Temos dados iteráveis

# Temos: a1, a2, a3...

# Função: f(x)

# Utilizamos a função map(f, dados) onde o map irá mapear cada elemento dos dados e aplicara função.

# Map Object: f(a1), f(a2), f(a3)

# Mais um exemplo
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Tokio', 26), ('Nova York', 28)]
print(cidades)

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))
