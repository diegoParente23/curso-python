"""
Reduce

- A partir do python3 + a função Reduce não é mais uma função integrada
    - Agora temos que importar e utilizar a função a partir do módulo 'functools'

Guido van Rossum: Utilize a função reduce() se você realmente precisar dela, Em todo caso
99% das vezes um loop for é mais legivel

* Assim como o map e filter, recebe dois paramêtros, função e dados

Funciona da seguinte forma
    1° Passo
        - res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
    2° Passo
        - res2 = f(res1, a3) # Aplica a função passando o resultado do passo 1 mais o resultao do passo 2
    N° Passo
        - resn = f(resn, an, ...)
Ou seja em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior. No finak
reduce() irá retornar o resultado final

Alternativamente, poderiamos ver a função reduce() como:
funcao(funcao(funcao(a1, a2), a3), a4), ...), an)
"""
from functools import reduce

dados = [2, 3, 4, 1, 5, 6, 3, 4, 5, 8, 3]

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Utilizando um loop
res = 1
for n in dados:
    res *= n

print(res)
