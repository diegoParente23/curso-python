"""
List Comprehension

- Nós podemos adicionar estruturas condicionais lógicas para as nossas listas
"""
# Exemplos
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([numero for numero in numeros if numero % 2 == 0])
print([numero for numero in numeros if numero % 2 != 0])

# Refatorar
# OBS: Qualquer número par módulo de 2 é 0 e 0 em python é False. not False = True
print([numero for numero in numeros if not numero % 2])
print([numero for numero in numeros if numero % 2])

print([numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros])

print([numero for numero in [2, -1, 2, -2, -3, -4, 9, 8] if numero < 0])
