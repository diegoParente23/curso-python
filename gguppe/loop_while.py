"""
Loop while

while expressão_booleana
    // Execução
"""

# Exmplo 1
numero = 1

while numero < 10:
    print(numero)
    numero += 1

# Exemplo

resposta = 'não'

while resposta != 'sim':
    resposta = input('Já acabou ? ')

# Exemplo 3

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Saindo do for')

# Exemplo 4

while True:
    comando = input('Digite sair para sair: ')
    if comando == 'sair':
        break
