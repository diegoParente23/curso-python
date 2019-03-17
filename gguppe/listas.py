"""
Listas (list)

Listas em python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e também de podermos colocar qualquer tipo de dado.

- Dinâmico: Não possui tamnho fixo, ou seja podemos criar a lista e simplismente ir adicionando elementos;
- Qualquer tipo de dado: não possuem tipo de dado fixo, ou seja podemos colocar qualquer tipo de dados

As listas em python são representadas por colchetes: []

# Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)
"""

lista1 = [1, 90, 87, 25, 42, 71, 36, 44, 52]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

print(lista4)

print(lista5)

# Podemos facilmente checar se um determinado valor está em uma lista
num = 18

if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

lista1.sort()

print(lista1)

# Podemos facilmente conta o número de ocorrênci de um valor em uma lista

print(lista1.count(1))

print(lista5.count('e'))

# Adicionar elementos em uma lista
# Com o append só conseguimos incluir apenas um elemento por vez

# Coloca a lista como um elemento único (sublista)
# Mesmo resultado obtido no 'Add' das coleções do C#
lista1.append(42)
lista1.append(100)

lista1.sort()

print(lista1)

lista1.append([57, 101, 208, 398])

print(lista1)

if [57, 101, 208, 398] in lista1:
    print('Encontrei a lista')

# Coloca cada elemento da lista como um novo membro individual
# Mesmo resultado obtido no 'AddRange' das coleções do C#
lista1.extend([123, 44, 67])
lista1.extend('Geek University')

print(lista1)

# Podemos adicionar o item informando a posição na lista atravez do indice
# OBS: Isso não substitui o valor inicial, o mesmo será deslocado para a direita da lista
lista1.insert(2, 'Novo Valor')

print(lista1)

# Podemos facilmente juntar duas listas
lista6 = lista1 + lista2
lista6.extend(lista4)

print(lista6)

# Reverse na lista
lista2.reverse()

print(lista2)

# Podemos facilmente copiar uma lista
lista7 = lista2.copy()

print(lista7)

# Contando a quantidade de elementos da lista

print(f'Quantidade de elementos: {len(lista1)}')
print(f'Quantidade de elementos: {len(lista2)}')
print(f'Quantidade de elementos: {len(lista3)}')
print(f'Quantidade de elementos: {len(lista4)}')

# Podemos remover facilmente o último elemento de uma lista
lista8 = lista5.copy()
print(lista8)
lista5.pop()
print(lista8)

# Podemos remover um elemento pelo indice
# OBS: Os elementos a direita serão deslocados para a esquerda.
lista8.pop(2)
print(lista8)

lista8.pop(lista8.index('G'))
print(lista8)

# Podemos remover todos os elementos da lista
lista9 = lista5.copy()
print(lista9)
lista9.clear()
print(lista9)

# Podemos facilmente repetir elementos em uma lista
lista10 = lista5.copy()
lista10 = lista10 * 3
print(lista10)

# Podemos facilmente converter uma string para uma lista
# OBS: Por padrão o split separa os elementos pelos espaços entre eles
curso = 'Programação inicial programação em python'
print(curso)
curso = curso.split()
print(curso)

# Exemplo 2
curso = 'P,rograma,çãoinicial,em,program,ação,python'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em string
lista11 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista11)

# Abaixo estamos falando pega a lista11 coloca os espaços entre cada elemento e transforma em uma string
curso = ' '.join(lista11)
print(curso)

# Exemplo 2: Com '$' ao invés de ' '
curso = '$'.join(lista11)
print(curso)

# Com vários tipos diferentes de dados
lista12 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45369857422]
print(lista12)

# Iterando sobre listas
# Exemplo 1

for elemento in lista12:
    print(f'Elemento: {elemento}')

# Utilizando variáveis em listas

numeros = []
num1 = 1
num2 = 2
num3 = 3

numeros = [num1, num2, num3]
print(numeros)

# Fazemos acesso aos elementos de forma indexada
#           0         1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])
print(cores[1])
print(cores[2])
print()

# Fazer acesso aos elementos da lista inversa
# Para entender melhor o indice negativo, pense na lista como roda ou circulo
# Onde o final de um elemento está ligado ao inicio da mesma

print(cores[-1])
print(cores[-2])
print(cores[-3])
print()

for cor in cores:
    print(cor)

print()

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

print()

for indice, cor in enumerate(cores):
    print(indice, cor)

print()

# Outros métodos menos importantes mas úteis

# Encontrar o indice de um elemento na lista
# OBS Caso não tenha este elemento na lista será apresentado erro
numeros = [5, 6, 5, 7, 8, 9, 10, 5, 5]
print(f'Indice: {numeros.index(10)}')

# Se o valor estiver duplicado o mesmo trará a primeira ocorrência
print(f'Indice: {numeros.index(5)}')

# Podemos fazer buscas dentro de um range, ou seja, qual indice começar a buscar.
# buscando a partir do indice 1
print(numeros.index(5, 1))

# buscando a partir do indice 3
print(numeros.index(5, 3))

# Podemos fazer buscas dentro de um range, inicio e fim
# buscando do indice 1 até 7
print(numeros.index(5, 1, 7))

print()

# Revisar Slicing
# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com slice de lista com parâmetro 'inicio'
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

# Pegando todos os elementos
print(lista1[::])

# Iniciando no indice 1 e pegando todos os elementos restantes
print(lista1[1:])

# Trabalhando com slice de lista com parâmetro 'fim'
# Iniciando do 0 pegando até o indice 5
print((lista1[:5]))

# Iniciando do 1 pegando até o indice 5
print((lista1[1:5]))

# Iniciando do 1 pegando até o indice 5 Negativo
print((lista1[1:-5]))

# Trabalhando com slice de lista com parâmetro 'passo'
# Iniciando do 0 pegando até o indice 10 ao passo de 2 em 2
print((lista1[:10:2]))

# Iniciando do 0 pegando até o indice 10 ao passo de 2 em 2 Negativo
print((lista1[:-10:2]))

# Iniciando do 3 pegando até o indice 20 ao passo de 3 em 3
print((lista1[3:20:3]))

print()

nomes = ['Geek', 'University']
nomes.reverse()
print(nomes)

print()

# Soma*, Valor máximo*, Valor Minimo*, Tamnho
# * Se os valores forem todos inteiros ou reais
print(sum(lista1))
print(max(lista1))
print(min(lista1))
print(len(lista1))

print()

# Transformar uma lista em tupla

print(lista1)
print(type(lista1))

tupla = tuple(lista1)
print(tupla)
print(type(tupla))

print()

# Desempacotamento de listas
# Não podemos ter mais elementos para desempacotar do que a quantidade de variáveis
lista = [1, 2, 3]
num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# Copiando uma lista para outra (Shallow Copy e Deep Copy)
# Forma 1 Deep Copy
# Veja que ao utilizarmos o list.copy() copiamos os dados da lista para uma nova
# mantendo as duas independentes
# isso é chamado de Deep Copy ou cópia profunda
nova = lista1.copy()
print(nova)

nova.append(4)
print(lista1)
print(nova)

# Forma 2 Shallow Copy
# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova
# Mas após ao realizarmos a modificação em uma das listas, essa modificação refletiu ambas as listas
# isso é chamado de Shallow Copy
nova = lista1
print(nova)

nova.append(4)
print(lista1)
print(nova)
