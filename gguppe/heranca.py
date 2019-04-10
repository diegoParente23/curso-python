"""
POO - Herança(Inheritence)

A ideida de reaproveitar código e extender as classes

OBS: Com a herança a partir de uma classe existente, nós extendemos outra classe que passa a herdar atributos e métodos
da classe herdada

- Quando uma classe herda de outra classe, a classa herdada pe conhecida por:
    - Super classe
    - Classe mãe
    - Classe pai
    - Classe base
    - Classe genérica

- Quando uma classe herda de outra classe, ela é chamada de;
    - Sub classe
    - Classe filha
"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def get_nome(self):
        return self.__nome

    def to_string(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self, nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.__renda = renda

    def to_string(self):
        return f'Cliente renda: {self.__renda} nome: {self.get_nome()}'


class Funcionario(Pessoa):
    """Funcionário herda de pessoa"""
    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def to_string(self):
        return f'Funcionário matricula: {self.__matricula} nome: {self.get_nome()}'


# Overridade de Métodos (Overriding

cliente1 = Cliente('Diego', 'Parente', '385.401.828-23', 1000)
funcionario1 = Funcionario('Helena', 'Jones', '552251', 1000)

print(cliente1.to_string())
print(funcionario1.to_string())
