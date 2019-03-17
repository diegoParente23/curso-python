"""
Módulo Collections - Deque

https://docs.python.org/3/library/collections.html#collections.deque

- É uma lista de alta performance
"""

# Fazendo import
from collections import deque

# Criando deques
deq = deque('Geek')
print(deq)

# Adicionando elementos no deque
# OBS: Adiciona no final da lista
deq.append('y')
print(deq)

# Adicionando no começo da lista
deq.appendleft('y')
print(deq)

# Removendo elementos, sempre do final
deq.pop()
print(deq)

# Removendo elementos, sempre do inicio
deq.popleft()
print(deq)
