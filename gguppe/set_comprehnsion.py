"""
Set Comprehnsion

"""
# Exemplos
numeros = {num for num in range(1, 7)}
print(numeros)

# Outro exemplo
numeros = {num ** 2 for num in range(1, 5)}
print(numeros)

# D E S A F I O
dicionario = {chave: chave ** 2 for chave in numeros}
print(dicionario)

# Para finalizar
letras = {letra for letra in 'Geek University'}
print(letras)
