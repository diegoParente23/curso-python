"""
Módulo Collections - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

- Ao criar um dict utilizando o Default Dict, nós informamos um valor default
podendo usar lambda para isso, esse valor será utilizado sempre que não houver
um valor definido. Caso tentamos acessar uma chave que não existe, essa chave será
criada e o valor default será criado
"""

# Fazendo import
from collections import defaultdict

# Recap dict
dicionario = {'curso': 'Programação em Python Essencial'}
print(dicionario)
print(dicionario['curso'])

dicionario = defaultdict(lambda: 'Sem curso')

print(dicionario)
print(type(dicionario))

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)
print(dicionario['outro'])

print(dicionario)
