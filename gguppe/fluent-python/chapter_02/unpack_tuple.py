import os

result = divmod(20, 8)

print(result)

t = (20, 8)

result = divmod(*t)

print(result)

quotient, reminder = divmod(*t)

print(f'{quotient} {reminder}')

_, filename = os.path.split('/home/diegoparente/Downloads/Yu-Gi-Oh! GX - The Beginning of Destiny (USA).iso')

print(filename)

a, b, *rest = range(5)

print(f'({a}, {b}, {rest})')

a, b, *rest = range(3)

print(f'({a}, {b}, {rest})')

a, b, *rest = range(2)

print(f'({a}, {b}, {rest})')

a, *body, c, d = range(5)

print(f'({a}, {body}, {c}, {d})')

*head, b, c, d = range(5)

print(f'({head}, {b}, {c}, {d})')
