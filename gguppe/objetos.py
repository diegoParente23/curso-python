"""
POO - Objetos

Objetos -> São instâncias da classe, ou seja, após o mapeamento de objeto do mundo real para sua representação
computacional, devemos poder criar quantas instâncias forem necesárias. Podemos pensar em objetos/instâncias de uma
classe como variáveis do tipo definido na classe.
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar(self):
        self.__ligada = True

    def desligar(self):
        self.__ligada = False


class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def to_string(self):
        return f'Nome {self.__nome} Documento: {self.__cpf}'


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def show_customer(self):
        print(f'O cliente é {self.__cliente.to_string()}')


class Produto:

    def __init__(self, nome, descricao, valor):
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100


from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    id = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Temos {cls.id} usuário(s) no sistema.')

    @staticmethod
    def definicao():
        return 'UXB2340'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.id + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=20000, salt_size=16)
        Usuario.id = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def to_string(self):
        return f'{self.__nome} {self.__sobrenome}'

    def check_password(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


# Instância do Objeto
lamp1 = Lampada('branca', 110, 60)
print(f'A lampada está ligada ? {lamp1.checa_lampada()}')
lamp1.ligar()
print(f'A lampada está ligada ? {lamp1.checa_lampada()}')

user1 = Usuario('Diego', 'Parente', 'diego.parente@d.com.br', '123456')

cl1 = Cliente('Diego Parente', '38540182823')
cc = ContaCorrente(5000, 10000, cl1)
cc.show_customer()
