"""
Dictionary Comprehnsion

Pense o seguinte:
- Se quisermos criar uma list
lista = [1, 2, 3, 4, 5, 6, 7, 8]

- Se quisermos criar uma tuple
tupla = (1, 2, 3, 4, 5, 6, 7, 8)

- Se quisermos criar um set
conjuntos = {1, 2, 3, 4, 5, 6, 7, 8}

- Se quisermos criar um dict
dicionario = {a=1, b=2, c=3}

# Sintaxe
{chave: valor for in iterável}
"""
# Exemplos
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'f': 5}
print(numeros)

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)

numeros = [1, 2, 3, 4, 5]
print(numeros)

quadrado = {valor: valor ** 3 for valor in numeros}
print(quadrado)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo com lógica condicional
numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)
