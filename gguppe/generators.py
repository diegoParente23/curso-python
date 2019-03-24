"""
Generator Expression

Em aulas anteriores nós estudamos
    - List Comprehnsion
    - Dictionary Comprehnsion
    - Set Comprehnsions

Não vimos:
    - Tuple Generators... porque elas se chamam Generators

- É mais recomendado utilizar Generator se caso não for utilizar a lista que está sendo objeto da função
caso tenha que utilizar pode usar o List Comprehension
"""
from sys import getsizeof
nomes = ['Carlos', 'Camila', 'Carla', 'Catiana']

# Definição
res = (nome[0] == 'C' for nome in nomes)
print(res)
print(type(res))

# Exemplo 1
print(any(res))

# Exemplo 2 simplificando
print(any(nome[0] == 'C' for nome in nomes))

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Generator
# Ocupa menos recurso em memória
res = (nome[0] == 'C' for nome in nomes)
print(type(res))

# getsizeof() -> Retorna a quantidade em bytes em memória de um elemento como paramêtro

# Mostra quantos bytes a string 'Geek' está ocupando em memória. Quanto maior a string, mais espaço ocupa
print(getsizeof('Geek'))
print(getsizeof('Geek University'))
print(getsizeof(9))
print(getsizeof(99))
print(getsizeof(999))
print(getsizeof(99925893652446))
print(getsizeof(True))

print()

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dict Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para realizar a mesma tarefa, gastamos em memória:')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dict Comprehension: {dict_comp} bytes')
print(f'Generator Expression: {gen} bytes')

# Eu posso iterar no generator expressetion ? Sim!
gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)
