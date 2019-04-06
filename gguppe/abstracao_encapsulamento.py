"""
POO - Abstração e Encapsulamento

O grando objeto da orientação de objetos é encapsualar o nosso código dentro de um grupo lógico e hierárquico utilizando
classes.

Encapsular -> cápsula.

Abstração, em POO é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos privados
de usuário.
"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def transferir(self, valor, conta_destino):
        self.sacar(valor)
        conta_destino.depoistar(valor)

    def depoistar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('Valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if valor >= self.__saldo:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
        else:
            print('O valor deve ser maior que 0')

    def to_string(self):
        return f'Conta número: {self.__numero} titular: {self.__titular}'


# Testando
conta1 = Conta('Diego', 1000, 2000)
conta1.depoistar(150)
conta1.sacar(90)
print(conta1.to_string())
conta1.extrato()
print(conta1.__dict__)

print()

conta2 = Conta('Helena', 100, 200)
conta2.extrato()
conta2.transferir(100, conta1)

conta1.extrato()
conta2.extrato()
