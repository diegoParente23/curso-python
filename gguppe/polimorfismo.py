"""
POO - Polimorfismo

Poli -> Muitas
Morfis -> Formas
"""


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    @property
    def get_nome(self):
        return self.__nome

    def falar(self):
        raise NotImplemented('A classe filha deve implementar o método')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f'{self.get_nome} fala wau-wau!'


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f'{self.get_nome} fala miau-miau!'


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        return f'{self.get_nome} roe'


# Testes
felix = Gato('Felix')
print(felix.comer())
print(felix.falar())
print()

mickey = Rato('Mickey')
print(mickey.comer())
print(mickey.falar())
print()

pluto = Cachorro('Pluto')
print(pluto.comer())
print(pluto.falar())
print()
