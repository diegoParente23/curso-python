#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Doctests

- São testes que colocamos no doc string dos métodos python.

# Para rodar os testes no console
python -m doctest -v doctests.py

# Resultado:
Trying:
    soma(1, 2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.

def soma(a, b):
    #Soma os números a e b
    #>>> soma(1, 2)
    #3
    #>>> soma(4, 6)
    #10
    #return a + b


# Outro exemplo aplicando o TDD

def duplicar_valores(valores):
    #Duplicar valores
    #>>> duplicar_valores([1, 2, 3, 4, 5])
    #[2, 4, 6, 8, 10]
    #>>> duplicar_valores([])
    #[]
    #>>> duplicar_valores(['a', 'b', 'c', 'd'])
    #['aa', 'bb', 'cc', 'dd']
    #>>> duplicar_valores([True, None])
    #Traceback (most recent call last):
    #   ...
    #TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    #:param valores:
    #:return: valores duplicados
    #return [2 * elemento for elemento in valores]

# OBS: Dentro do docstring, o Python não reconhece string com aspas duplas. Precisa ser apas simples.
# Erro inesperado

def fala_oi():
    #Fala Oi
    #>>> fala_oi()
    'Oi'
    #
    #return 'Oi'
"""
# Último caso estranho


def verdade():
    """Retorna verdade
    >>> verdade()
    True
    """
    return True

