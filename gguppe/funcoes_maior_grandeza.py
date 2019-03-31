"""
Higher Order Function - HOF

Quando uma linguagem suporta este conceito, indica que podemos ter funções que retornam outras funções como resultado
ou podemos passar funções como argumentos para funções, ou até mesmo criar variáveis do tipo de funções

OBS: Em Python as funções são cidadões de primeira classe em ingles First Citzens
"""
# Exemplos:
# Definindo algumas funções


def somar(a, b):
    return a + b


def diminur(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, func):
    return func(num1, num2)


# Testando as funções
print(calcular(1, 4, somar))
print(calcular(4, 2, diminur))
print(calcular(4, 2, dividir))
print(calcular(1, 4, multiplicar))

# Nested Functions(Inner Functions) -> Funções Aninhadas
# Em Python também podemos ter funções dentro de funções
from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa


# Testando
print(cumprimento('Diego'))
print(cumprimento('Henrique'))
print(cumprimento('Astolfo'))

# Retornando funções dentro de outras funções


def faz_me_rir():
    def rir():
        return choice(('hahahaha', 'kkkkk', 'yayayayaya'))
    return rir


# Testando
rindo = faz_me_rir()
print(rindo())

# Inner Functions (Funções internas / Nested Functions) podem acessar o escopo de funções externas


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahaha', 'lolololololo', 'kkkkkkkk'))
        return f'{risada} {pessoa}'
    return dando_risada


rindo = faz_me_rir_novamente('Diego')
print(rindo())
