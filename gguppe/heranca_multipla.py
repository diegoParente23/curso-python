"""
POO - Herança Multipla

- Nada mais é do que a possibilidade de uma classe herdar de multiplas classe, fazendo com que a classe filha
herde todos os atributos e métodos de todas as classes.
- Pode ser feita de duas maneiras
    - Por Multiderivação direta
    - Por Multiderivação indireta
- MRO -> Method Resolution Order

# Exemplo 1 Multiderivação direta


class Base1:
    pass


class Base2:
    pass


class Multiderivada(Base1, Base2):
    pass

# Exemplo 2 Multiderivação indireta


class Base3(Base2):
    pass


class Base4(Base3):
    pass


class Multiderivada2(Base4):
    pass
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


baleia = Aquatico('Wally')
print(baleia.cumprimentar())
print(baleia.nadar())
print()

leao = Terrestre('Jonas')
print(leao.cumprimentar())
print(leao.andar())
print()

pinguim = Pinguim('Euclides')
print(pinguim.cumprimentar())
print(pinguim.nadar())
print(pinguim.andar())
print()

# Objeto de instância de ?...
print(f'Wally é instância de Áquatico ? {isinstance(baleia, Aquatico)}')
print(f'Euclides é instância de Pinguim ? {isinstance(pinguim, Pinguim)}')
print(f'Euclides é instância de Áquatico ? {isinstance(pinguim, Aquatico)}')
print(f'Euclides é instância de Terrestre ? {isinstance(pinguim, Terrestre)}')
print(f'Euclides é instância de Aninal ? {isinstance(pinguim, Animal)}')
print(f'Euclides é instância de object ? {isinstance(pinguim, object)}')
print(f'Jonas é instância de Terrestre ? {isinstance(leao, Terrestre)}')
