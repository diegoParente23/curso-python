"""
Pacotes

Módulo -> É apenas um arquivo Python que pode ter diversas funções para utilizarmos
Pacote -> É um direatório contendo uma coleção de módulos

OBS: Nas versões 2.x do Python, um pacote Python deveria conter dentro dele um arquivo chamado __init__.py
mas normalmente é utilizado para manter compatibilidade.
"""
from geek import geek1, geek2
from geek.university import geek3, geek4

print(geek1.pi)
print(geek1.funcao1(1, 5))
print(geek2.curso)
print(geek2.funcao2())
print(geek4.funcao4())
print(geek3.funcao3())
