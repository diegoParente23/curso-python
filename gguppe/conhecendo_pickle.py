#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Conhecendo Pickle

A função do pickle é realizar o seguinte processo:

Objeto Python -> Binarização
Binárização -> Objeto Python

Este processo é chamado de serialização/deserialização

# OBS: O módulo Pickle não é seguro contra dados maliciósos e desta forma
não é recomendado trabalhar com arquivos pickle vindo de outras pessoas
que você não conheça ou de fontes desconhecidas

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
        return f'{self.__nome} está comendo...'


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        return f'{self.nome} está latindo'


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
