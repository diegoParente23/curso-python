#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Conhecendo Pickle

A fun��o do pickle � realizar o seguinte processo:

Objeto Python -> Binariza��o
Bin�riza��o -> Objeto Python

Este processo � chamado de serializa��o/deserializa��o

# OBS: O m�dulo Pickle n�o � seguro contra dados malici�sos e desta forma
n�o � recomendado trabalhar com arquivos pickle vindo de outras pessoas
que voc� n�o conhe�a ou de fontes desconhecidas

# Fazendo a escrita de arquivos pickles
with open('animais.pickle', 'wb') as arquivo:
    pickle.dump((felix, pluto), arquivo)
"""
import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        return f'{self.__nome} est� comendo...'


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} est� miando...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        return f'{self.nome} est� latindo'


felix = Gato('Felix')
pluto = Cachorro('Pluto')

# Fazendo a leitura de arquivos pickles
with open('animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(type(gato))
    print(f'O gato chama-se {gato.nome}')
    print(gato.mia())
    print(type(cachorro))
    print(f'O cachorro chama-se {cachorro.nome}')
    print(cachorro.late())
