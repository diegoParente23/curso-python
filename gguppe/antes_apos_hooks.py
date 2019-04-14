#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Unittest - Antes e ap�s hooks

hooks - s�o os testes em si. Ou seja, a execu��o dos testes.

setup() -> � executado antes de cada m�todo de teste. � �tili para criarmos inst�ncias de objetos e outros dados;
tearDown() -> � executado depois de cada teste. � �tili para excluirmos dados ou fechar conex�es com o banco
de dados
"""

from unittest import TestCase


class ModuloTest(TestCase):

    def setUp(self):
        # Configura��es do setUp()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste.
        # tearDown() vai rodar ap�s o teste
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste.
        # tearDown() vai rodar ap�s o teste
        pass

    def tearDown(self):
        # Configura��es do tearDown()
        pass
