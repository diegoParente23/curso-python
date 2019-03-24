"""
Len, Abs, Sum, Round

- abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria seu valor real sem sinal
- sum() -> Recebe como paramêtro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos
incluindo o valor
- round() -> Retorna para um número arredondado para n digitos de precisão após a casa decimal, Se a precissão não for
informada retorna o inteiro de entrada.
"""
# Len
print(len('Geek University'))
print(len([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(len((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
print(len({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}))
print(len({'a': 1, 'b': 2, 'c': 3}))

# Por debaixo dos panos o python faz o seguinte

# Dunder len
print('Geek University'.__len__())

# Abs
print(abs(-5))
print(abs(-10))
print(abs(10))
print(abs(3.14))
print(abs(-3.14))

# Sum
print(sum([1, 2, 3, 4, 5]))
print(sum({1, 2, 3, 4, 5, 5}))
print(sum((1, 2, 3, 4, 5)))
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))
print(sum([1, 2, 3, 4, 5], 5))
print(sum([3.14, 4.58, 5.87, 6.28]))

# Round
print(round(10.1))
print(round(3.05))
print(round(10.14))
print(round(10.144))
print(round(10.1445))
print(round(10.144478523, 2))
print(round(10.144478523, 3))
print(round(10.166778523586, 3))
