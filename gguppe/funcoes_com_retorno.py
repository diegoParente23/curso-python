"""
Funções com retorno

OBS: Quando uma função não retorna nenhum valor, o retorno é None
OBS: Não precisamos criar uma variável para receber o retorno de uma função
podemos passar o retorno para a execução de outras funções.

- Podemos retornar qualquer tipo de dado e multiplos valores

def computador():
    valor = random()
    if valor > 0 and valor <= 0.33:
        return 'Pedra'
    elif valor > 0.33 and valor <= 0.66:
        return 'Papel'
    else:
        return 'Tesoura'


def bind(opcao):
    if opcao == 1:
        return 'Papel'
    elif opcao == 2:
        return 'Tesoura'
    elif opcao == 3:
        return 'Pedra'


sair = ''
while sair != 'sair':
    print('Janken Po')
    opcao = int(input('Escolha sua opção ([1] para papel, [2] para tesoura e [3] para pedra) ou sair para sair: '))
    print(f'Adversário jogou: {computador()}')
    print(f'Resultado Você: {bind(opcao)} X {computador()} Adversário')
"""
# Vamos criar uma função para jogar uma moeda
from random import random

# Exemplos
numeros = [1, 2, 3]
ret_pop = numeros.pop()

print(f'Retorno do pop: {ret_pop}')
print(numeros)


# Criando
def quadrado_de_7():
    return 7 * 7


# Criamos uma variável para receber o retorno de uma função
retorno = quadrado_de_7()
print(f'Quadrado de 7 é: {retorno}')
print(f'Resultado: {quadrado_de_7() + 1}')


# Exemplo 2
def diz_oi():
    return 'Oi'


print(diz_oi())
print(f'{diz_oi()} Pedro')


# Exemplo 3
def nova_funcao():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_funcao())


# Exemplo 4
def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)
print(outra_funcao())


def joga_moeda():
    # Gera um número pseudo-randomico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara', valor
    return 'Coroa', valor


print(f'Foi jogado a moeda')
print(f'O Resultado foi: {joga_moeda()}')

# Erros comuns na utilização do retorno que na verdade não é erro e sim uma codificação desnecessária


def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False


print(eh_impar())
