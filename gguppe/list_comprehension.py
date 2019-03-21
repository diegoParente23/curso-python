"""
List Comprehension

- Utilizando list comprehension nós podemos gerar novas listas com dados processados
a partir de outro iterável

# Sintaxe

- [dado for dado in iteravel]

Para entender melhor

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10
"""
# Exemplo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = [numero * 10 for numero in numeros]
print(res)

res = [numero / 2 for numero in numeros]
print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)

print([numero * 2 for numero in numeros])
print([numero * 2 for numero in [1, 2, 3, 4, 5]])

nome = 'Geek University'
print([letra.upper() for letra in nome])

amigos = ['diego', 'julia', 'fabio', 'jonatan']
print([letra.title() for letra in amigos])

print([numero * 3 for numero in range(1, 10)])

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

print([str(numero) for numero in numeros])
