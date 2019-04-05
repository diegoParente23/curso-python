"""
POO - Métodos

- Funções, que representação comportamentos do objeto, ou seja, ações que este objeto pode realizar no seu sistema.
- Dividimos os métodos em dois grupos
    - Métodos de instância
    - Métodos de classe
- Métodos de classe são conhecidos como métodos estáticos em outras linguagens
- Para criar métodos privados, por conveção o método deve iniciar com '__'
- Métodos estáticos em python não possuem acesso nem a instância e nem a classe

- O método dunder init é um método especial, ele é um construtor

OBS: Todo elemento que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)
OBS: Os métodos/funções dunder em Python são métodos mágicos
OBS: A T E N Ç Ã O - Por mais que possamos criar métodos dunder, não é aconselhavel, o python possuí vários métodos com
essa nomenclatura, pode ser que mudemos os comportamentos desses métodos mágicos, de preferência nunca crie métodos
assim.

p1 = Produto('Playstation 4', 'Video Game', 2300)
print(p1.desconto(50))

us1 = Usuario('Diego', 'Parente', 'diego.parente@hbsis.com.br', '12345')
us2 = Usuario('Helena', 'Ruiz', 'helena.ruiz@hbsis.com.br', '12345')
print(us1.to_string())
print(us2.to_string())
print(Usuario.to_string(us1))

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a sus senha: ')

print()

if senha != confirma_senha:
    print('Senha não confere')
else:
    usuario = Usuario(nome=nome, sobrenome=sobrenome, email=email, senha=senha)
    print('Usuário criado com sucesso!')
    print()
    senha = input('Informe a senha de acesso: ')
    if usuario.check_password(senha=senha):
        print('Senha confere')
    else:
        print('Senha não confere')

    print(f'Sua senha é {usuario._Usuario__senha}')
"""
# Métodos de instância


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo


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


# Métodos de classe
user = Usuario('Felicity', 'Jones', 'felicity.jone@marvel.com', '123456')

# Forma correta
Usuario.conta_usuarios()

# Forma possível mas incorreto
user.conta_usuarios()

# Métodos Estáticos
print(Usuario.id)
print(Usuario.definicao())
user = Usuario('Diego', 'Parente', 'diego.parente@d.com.br', '123456')
print(user.id)
print(Usuario.definicao())
