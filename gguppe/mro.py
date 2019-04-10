"""
POO - MRO -> Method Resolution Order

- É a ordem de execução dos métodos, ou seja, quem será executado primeiro
- Podemos conferir a ordem de execução dos métodos de três formas:
    - Via propriedade da class __mro__
    - Via método mro()
    - Via help
"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def get_nome(self):
        return self.__nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self.get_nome} está nadando.'

    def cumprimentar(self):
        return f'Eu sou {self.get_nome} do mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self.get_nome} está andando!'

    def cumprimentar(self):
        return f'Eu sou {self.get_nome} da terra!'


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)


# Testando
pinguim = Pinguim('Euclides')
print(pinguim.cumprimentar())
print()
