"""
Estruturas condicionais
if, else elif
"""

idade = int(input('Qual é sua idade ? '))

if idade < 18:
    print(f'Menor de idade {idade} anos')
elif idade == 18:
    print(f'Acabou de atingir a maioridade {idade} anos')
else:
    print(f'Maior de idade {idade} anos')
