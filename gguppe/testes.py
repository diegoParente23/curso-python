#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import unittest

from atividades import comer, dormir, eh_engracada


class AtividadesTestes(unittest.TestCase):

    def test_commer_saudavel(self):
        """Testando o retorno com comida saud�vel"""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo porque quero manter a forma'
        )

    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa"""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque a gente s� vive uma vez'
        )

    def test_dormir_pouco(self):
        """Testando o retorno dormindo pouco"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado ap�s dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito"""
        self.assertEqual(
            dormir(10),
            'Ptz! Dormi muito! Estou atrasado para o trabalho'
        )

    def test_eh_engracada(self):
        """Testando o retorno de eh_engracada"""
        #self.assertEqual(eh_engracada('S�rgio Malandro'), False)
        self.assertFalse(eh_engracada(pessoa='S�rgio Malandro'))
        self.assertTrue(eh_engracada(pessoa='Jim Carrey'), 'Jim Carrey deveria ser engra�ado')


if __name__ == '__main__':
    unittest.main()
