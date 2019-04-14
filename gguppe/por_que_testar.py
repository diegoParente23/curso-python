#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Por que testar nosso código ?
    - Reduzir bugs
    - Testes garatem que novos recursos da sua aplicação não quebrem recursos antigos;
    - Testes garatem que bugs (problemas) que foram corrigidos anteriormente, continue corrigidos;
    - Testes garatem que a refatoração de código que costumamos fazer não tragam novos bugs (problemas);

Com TDD é utilizado estágios de desenvolvimento:
    - Você escreve seu teste primeiro;
    - Então você escreve o código mínimo suficiente para fazer o teste passar (ou seja, executar com sucesso);
    - Então refatora o código para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe, o recurso é considerado completo;

Estes estágios de desenvolvimento do TDD são quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red;
    - Green;
    - Refactor

Teste Automátizado

"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        return f'{self.__nome} está miando...'


felix = Gato('Felix')
print(felix.miar())
