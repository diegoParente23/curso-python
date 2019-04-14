#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Assertions (Afirma��es/Checagens/Questionamentos)

Em Python utilizamos a palavra reservada assert para realizar uma simples afirma��o utilizadas no testes.

Utilizamos assert em uma express�o que queremos checar se � v�lida ou n�o.
Se a express�o for verdadeira, retorna None e caso seja falsa levanta erro
tipo AssertionError.

# OBS N�s podemos especificar, opcionalmente um segundo argumento ou mesmo uma mensagem.
de erro personalizado.

# OBS A palavra 'assert' pode ser utilizada em qualquer fun��o ou c�digo nosso... n�o precisa ser exclusivamente
nos testes.

# OBS: Se o program Python for executado com o param�tro -o, nenhum assertion ser� executado.
"""


def soma_numeros_positivo(a, b):
    # Mesma coisa que a > b and b > 0
    assert a > b > 0, 'Ambos os n�meros precisa ser positivo'
    return a + b


# Valido
# ret = soma_numeros_positivo(2, 4)
# Inv�lido AssertionError
# ret = soma_numeros_positivo(-2, 4)
# print(ret)

def comer_fast_fodd(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente',
    ], 'A comida precisa ser fast-food'
    return f'Eu estou comendo {comida}'


comida = input('O que deseja comer ? ')
print(comer_fast_fodd(comida))

# A L E R T A: Cuidado ao utilizar 'assert'
# OBS: Se o program Python for executado com o param�tro -o, nenhum assertion ser� executado.
