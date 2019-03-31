"""
Funções com Paramêtros (de entrada)

- Funções que recebem dados para processamento
- entrada -> processamento -> saída
- Funções podem ter N paramêtros de entrada
- Paramêtros são variáveis declaradas na definição de uma função
- Argumento são dados passados durante a execução de uma função
- A ordem dos paramêtros importa

# Refatorando uma função


def quadrado(numero):
    # return numero * numero
    return numero ** 2


print(quadrado(7))
print(quadrado(5))
print(quadrado(8))


# Exemplo 2
def cantar_parabens(aniversariante):
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva a(o) {aniversariante}')


cantar_parabens('Diego')


def soma(a, b):
    return a + b


def multiplica(a, b):
    return a * b


def outra(a, b, msg):
    return (a + b) * msg


print(soma(10, 3))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 1, 'Hello World '))
print(outra(3, 1, 'Geek '))


# Nomeado paramêtros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Diego', 'Parente'))

# Argumentos nomeados (Keyword Arguments)
# Caso utilizarmos nomes dos parametros nos argumentos, para informa-los, podemos
# utilizar qualquer ordem
print(nome_completo(nome='Diego', sobrenome='Parente'))
print(nome_completo(sobrenome='Parente', nome='Diego'))
"""


# Erros comuns na utilização do return
def somar_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


if __name__ == '__main__':
    print(somar_impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(somar_impares([1, 2, 3, 4, 5, 6, 7, 8]))
    print(somar_impares([1, 2, 3, 4, 5, 6, 7]))
else:
    print('O módulo python foi importado')
