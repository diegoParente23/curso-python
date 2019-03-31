"""
Teste de velocidade com funções geradoras

# Generators (Geradores)


def nums():
    for num in range(1, 10):
        yield num


gen = nums()
print(gen)

print(next(gen))
print(next(gen))
print(next(gen))

# Generator Expression
gen2 = (num for num in range(1, 10))
print(gen2)
print(next(gen2))
print(next(gen2))

print(sum(num for num in range(1, 10)))
"""
# Realizando o teste de velocidade
import time

# Generator Expression
gen_inicio = time.time()
print(sum(num for num in range(100000000)))
gen_tempo = time.time() - gen_inicio

# Lista Comprehension
lista_inicio = time.time()
print(sum([num for num in range(100000000)]))
lista_tempo = time.time() - lista_inicio

print()

print(f'Generator Expression Time: {gen_tempo}')
print(f'List Comprehnsion Time: {lista_tempo}')
