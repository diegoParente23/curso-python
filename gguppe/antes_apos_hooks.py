#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Unittest - Antes e após hooks

hooks - são os testes em si. Ou seja, a execução dos testes.

setup() -> é executado antes de cada método de teste. É útili para criarmos instâncias de objetos e outros dados;
tearDown() -> é executado depois de cada teste. É útili para excluirmos dados ou fechar conexões com o banco
de dados
"""

from unittest import TestCase


class ModuloTest(TestCase):

    def setUp(self):
        # Configurações do setUp()
        pass

    def test_primeiro(self):
        # setUp vai rodar antes do teste.
        # tearDown() vai rodar após o teste
        pass

    def test_segundo(self):
        # setUp vai rodar antes do teste.
        # tearDown() vai rodar após o teste
        pass

    def tearDown(self):
        # Configurações do tearDown()
        pass
