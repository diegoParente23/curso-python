#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Por que testar nosso c�digo ?
    - Reduzir bugs
    - Testes garatem que novos recursos da sua aplica��o n�o quebrem recursos antigos;
    - Testes garatem que bugs (problemas) que foram corrigidos anteriormente, continue corrigidos;
    - Testes garatem que a refatora��o de c�digo que costumamos fazer n�o tragam novos bugs (problemas);

Com TDD � utilizado est�gios de desenvolvimento:
    - Voc� escreve seu teste primeiro;
    - Ent�o voc� escreve o c�digo m�nimo suficiente para fazer o teste passar (ou seja, executar com sucesso);
    - Ent�o refatora o c�digo para realizar a funcionalidade e testa novamente;
    - Uma vez que o teste passe, o recurso � considerado completo;

Estes est�gios de desenvolvimento do TDD s�o quase como um mantra que os desenvolvedores seguem, conhecidos como:
    - Red;
    - Green;
    - Refactor

Teste Autom�tizado

"""


class Gato:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def miar(self):
        return f'{self.__nome} est� miando...'


felix = Gato('Felix')
print(felix.miar())
