"""
Lambdas

Conhecidas por expressões lambdas ou só lambdas, são funções sem nomes, ou seja funções anonimas
- Expressão lambdas podem receber 'n' paramêtros
"""
# Exemplo


def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))

# Exemplo de lambda
lambda x: 3 * x + 1

# Como utilizar a expressão lambda
calc = lambda x: 3 * x + 1

print(calc(2))
print(calc(9))

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' Diego Henrque ', ' costa parente '))
print(nome_completo(' angelia ', ' jolie'))

# Em funções Python podemos ter nenhuma ou várias entradas
amar = lambda: 'Como não amar Phyton'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / 2)

print(amar())
print(uma(3))
print(duas(4, 50))
print(tres(3, 6, 19))

# Outro exemplo
autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Artur C. Clark', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)

# Função Quadrática
def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))
print(geradora_funcao_quadratica(3, 0, 3)(2))
