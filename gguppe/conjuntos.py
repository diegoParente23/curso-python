"""
Conjuntos

- Conjuntos estamos fazendo referência a teoria dos conjuntos da matemática

- São chamados de sets, da mesma forma da matemáticas;
    - Sets (conjuntos) não possuem valores duplicados
    - Sets (conjuntos) não possuem valores ordenados
    - Elementos não são acessados via indice, ou seja, conjuntos não são indexados

- Sets são referenciados com {}

Diferenças entre conjuntos (sets) e dicionários (dict)
    - Um dict tem chave/valor
    - Um set tem apenas valor
"""

print(type(set()))

# Definindo um conjunto

# Forma 1
# OBS: Ao criar um conjunto, caso seja adicionado um valor duplicado
# O mesmo será ignorado e não vai gerar erro
s = set({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3})
print(type(s))
print(s)

# Forma 2 mais comum
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3}
print(s)

# Conversões para outros tipos de listas
lista = set('Geek University')
print(lista)

lista = set([1, 2, 3, 3, 3])
print(lista)

tupla = (1, 2, 3, 3)
tupla = set(tupla)
print(tupla)

# Podemos ver se contém um elemento no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem')

# Importante: Além de não termos valores duplicados não temos ordem
lista = [99, 2, 34, 10, 12, 34, 47, 75]
print(f'List: {lista} com quantidade: {len(lista)}')

tupla = (99, 2, 34, 10, 12, 34, 47, 75)
print(f'Tuple: {tupla} com quantidade: {len(tupla)}')

dictionary = {}.fromkeys(lista, 'none')
print(f'Dict: {dictionary} com quantidade: {len(dictionary)}')

tupla = (99, 2, 34, 10, 12, 34, 47, 75)
print(f'Tuple: {tupla} com quantidade: {len(tupla)}')

conjunto = {99, 2, 34, 10, 12, 34, 47, 75}
print(f'Set: {conjunto} com quantidade: {len(conjunto)}')

# Assim como todo outro tipo de lista podemos colocar qualquer tipo de dados no set
# ou seja, misturar os tipos como string, bool ou outro qualquer
s = {1, False, 'b', 34.34, 44}
print(s)

# Podemos iterar sobre os sets
for n in s:
    print(n)

# Usos interessantes dos sets
# Imagine que fizemos um cadastro em um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade e de onde vieram
cidades = ['Belo Horizonte', 'Rio de Janeiro', 'Fortaleza', 'Rio de Janeiro', 'Fortaleza']
print()
print(cidades)
print(f'Quantas pessoas visitaram o museum ? Resposta: {len(cidades)}')

# Agora precisamos saber quantas cidades distintas visitaram
print(f'Quantas cidades distintas ? {len(set(cidades))}')

# Adicionando um elemento ao conjunto
# OBS: Duplicidade não gera erro
s = {1, 2, 3}

s.add(4)
s.add(5)
s.add(1)

print(s)

# Remover elementos de um conjunto
print(s)

# Forma 1
# OBS: Não é indice informamos o valor que será removido
# OBS: Caso o valor não exista, será gerado um erro
s.remove(3)
# s.remove(33)

print(s)

# Forma 2
# OBS: Caso o valor não exista, não será gerado erro
s.discard(2)
s.discard(22)
print(s)

# Podemos remover todos os items
ss = s.copy()
print(ss)
ss.clear()
print(ss)

# Métodos matemáticos

# Imagine dois conjuntos um com estudantes do curso python e outro de java
# Veja que alguns alunos estudam python e java
estudantes_python = {'Diego', 'Gustavo', 'Julia', 'Ana', 'Patricia'}
estudantes_java = {'Fernanda', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}

# Precisamos gerar um conjunto com nomes de estudantes unicos

# Forma 1 - Union * Mais recomendado *
estudantes = estudantes_python.union(estudantes_java)
print(estudantes)

# Forma 2 - Utilizando o caracter pipe |
estudantes = estudantes_python | estudantes_java
print(estudantes)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Intersection
estudantes = estudantes_python.intersection(estudantes_java)
print(estudantes)

# Forma 2 - Utilizando &
estudantes = estudantes_python & estudantes_java
print(estudantes)

# Gerar um conjunto de estudantes que não estão no outro
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)


# Soma*, Valor máximo*, Valor Minimo*, Tamnho
# * Se os valores forem todos inteiros ou reais
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
