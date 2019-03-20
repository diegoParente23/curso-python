"""
Funções com paramêtros padrão (Default Parameters)

- Podemos utilizar qualquer tipo de dado como paramêtro opcional
"""


def quadrado(numero):
    return numero ** 2


print(quadrado(9))


def exponencial(numero=4, potencia=2):
    return numero ** potencia


print(exponencial(10, 3))
print(exponencial(10))
print(exponencial())


def mostrar_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostrar_informacao('Diego', True))
print(mostrar_informacao('Diego'))
print(mostrar_informacao(instrutor=True))
print(mostrar_informacao())


def soma(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


print(mat(2, 3))
print(mat(3, 3, sub))

# Escopo
# Variáveis globais e locais
# OBS: Se uma variável local tiver o mesmo nome que uma variável global, a local terá preferência
# A T E N Ç Ã O Evite utilizar variáveis globais
instrutor = 'Geek'


def diz_oi():
    # instrutor = 'Python'
    return f'Oi {instrutor}'


def diz_oi_2():
    prof = 'Geek'
    return f'Olá {prof}'


print(diz_oi_2())
# Erro pois não é possível acessar variável fora do escopo print(prof)

total = 0
"""
Erro pq não é possível realizar operação com variável que ainda não foi inicializada

def incrementa():
    total = total + 1
"""


# Funciona assim
def incrementa():
    # Avisando que queremos utilizar a variável global
    global total

    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())

# Podemos ter funções que são declaradas dentro de funções, e também  tem uma forma especial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador

        contador += 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())
