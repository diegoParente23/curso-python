"""
Tipo booleana

2 constantes true ou false

OBS: Sempre com a inicial maiuscula

True e False
"""

ativo = True
print(ativo)
print(type(ativo))

"""
Operações básicas
"""

# Negação (not):
print(not ativo)
ativo = not False
print(ativo)

# Ou (or):
print(True or True)
print(True or False)
print(False or True)
print(False or False)

logado = False

print(f"Ok? {ativo or logado}")

# E (and):
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Exemplos
print(f"{5} > {3} ? {5 > 3}")
print(f"{5} < {3} ? {5 < 3}")
print(f"{5} >= {3} ? {5 >= 3}")
print(f"{5} <= {3} ? {5 <= 3}")
print(f"{5} == {3} ? {5 == 3}")

print(f"{5} == {3} and {1} < {2} ? {5 == 3 and 1 < 2}")
print(f"{5} == {3} and {1} < {2} ? {5 == 3 or 1 < 2}")

