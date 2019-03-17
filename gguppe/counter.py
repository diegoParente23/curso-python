"""
Módulo Collections - Counter(Contador)

https://docs.python.org/3/library/collections.html#collections.Counter

Conhecidos -> High-Performance Container Datatypes

Counter -> Recebe um iteravel como param e cria um obj do tipo collection counter que é parecido como um
dicionário, contendo uma chave o elemento da lista passada como parametro e como valor a quantidade
de ocorrências desse elemento
"""
# Realizando o import
from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável aqui usamos lista
# Counter({1: 4, 2: 3, 4: 3, 8: 3, 5: 1, 6: 1, 7: 1, 9: 1})
# Veja que para cada elemento da lista o counter criou uma chave e
# colocou como valor a quantidade de ocorrência
lista = [1, 2, 1, 1, 2, 2, 1, 4, 4, 4, 5, 6, 7, 8, 8, 8, 9]
res = Counter(lista)

print(type(res))
print(res)

# Exemplo 2
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
print(Counter('Geek University'))

# Exemplo 3
texto = """Teoria dos conjuntos é o ramo da matemática que estuda conjuntos, que são coleções de elementos. 
Embora qualquer tipo de elemento possa ser reunido em um conjunto, a teoria dos conjuntos é aplicada na maioria 
das vezes a elementos que são relevantes para a matemática. A linguagem da teoria dos conjuntos pode ser usada nas 
definições de quase todos os elementos matemáticos."""
palavras = texto.split()
print(palavras)

res = Counter(palavras)
print(res)

# Pegando a quantidade de uma determinada palavra
print(res['teoria'])

# Pegando as 5 palavras com mais ocorrência no texto
print(res.most_common(10))
