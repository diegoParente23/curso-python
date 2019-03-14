"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais:

2 - Variáveis locais:
"""

# Variável Global
numero = 43
print(numero)
print(type(numero))

numero = "Diego"
print(numero)
print(type(numero))

numero = 50

if numero > 10:
    novo = numero + 10
    print(novo)

print(novo)
