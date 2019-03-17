"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem duas diferenças básicas

1 - tuplas são representadas por parenteses

2 - As tuplas são imutáveis: isso significa que ao criar uma tupla que ela não muda

OBS Por que usar tuplas ?

-> Tuplas são mais rápidos do que listas
-> Tuplas deixam o seu código mais seguro * Isso pq trabalhar com objs imutáveis traz segurança ao seu código
"""

print(type(()))

# Cuidado 1: As tuplas são representadas por parenteses '()', mas veja:

tupla1 = (1, 2, 3, 4, 5)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5
print(tupla1)
print(type(tupla2))

# Cuidado 2: Tuplas com 1 elemento
# Isso não é uma tupla e sim <class, int>
tupla3 = (4)
print(tupla3)
print(type(tupla3))

# Isso é uma tupla
tupla3 = (4,)
print(tupla3)
print(type(tupla3))

tupla3 = 4,
print(tupla3)
print(type(tupla3))

# Podemos concluir que tuplas são definidas pela virgula e não pelo uso dos parenteses '()'
# (4) -> Não é tupla
# (4,) -> É tupla
# 4, -> É tupla

# Podemos gerar uma tupla dinamicamente com range(inicio,fim,passo)
tupla = tuple(range(11))
print(tupla)

# Desempacotamento de tupla
tupla = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# OBS Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato que as tuplas são imutáveis

# Soma*, Valor máximo*, Valor minimo* e tamanho
# * Somente se os valores forem inteiros ou reais

tupla = (1, 2, 3, 4, 5)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas
tupla = (1, 2, 3)
tupla2 = (4, 5, 6)

print(tupla)
print(tupla2)

print(tupla + tupla2)

print(tupla)
print(tupla2)

# Tuplas são imutáveis mas podemos sobreescrever os valores
tupla = tupla + tupla2
print(tupla)

# Verificar se determinado elemento está na tupla
print(3 in tupla)

# Iterando sobre uma tupla
tupla = (1, 2, 3)

for n in tupla:
    print(n)

print()

for indice, valor in enumerate(tupla):
    print(indice, valor)

print()

# Contando elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')

print(tupla.count('a'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))

# Dicas na utilização da tuplas
# Devemos utilizar tuplas sempre que não precisarmos mudar os dados contidos em uma coleção

# Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro'
         , 'Dezembro')

for numero, mes in enumerate(meses):
    print(f'Mês: {numero + 1}, Nome: {mes}')

# Acessando via indice
print(meses[5])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i += 1

# Slicing
print(meses[1::2])
print(meses[::2])

