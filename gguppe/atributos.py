"""
POO - Atributos

- Representam as caracteristicas do objeto, ou seja pelos atributos conseguimos representar computacionalmente
os estados de um objeto.
- Por convenção em python ficou estabelecido que todo atributo de uma classe é público, ou seja pode ser acessado
em todo o projeto
- Caso queiramos transformar o atributo em privado, utiliza-se duplo underscore no ínicio do seu nome isso é conhecido
também como Name Mangling
- Lembrando que isso é apenas uma conveção, ou seja, a linguagem python não vai impedir que façamos acesso aos atributos
como privados fora da classe

- Em Python dividimos os atributos em 3 grupos
    - Atributos de Instância
    - Atributos de Classe
    - Atributos Dinâmicos

- Construtor
    - É um método especial utilizado para a construção do objeto
"""
# Atributos de instância
# Significa que ao criarmos instâncias de uma classe, todas as instâncias terão esses atributos


# Classes com atributos com atributos de instância publico
class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Classes com atributos privados
class Acesso:

    def __init__(self, email, senha):
        self.__email = email
        self.__senha = senha

    def get_senha(self):
        return self.__senha

    def get_email(self):
        return self.__email


# Exemplo de uso do atributo mesmo com o '__'
user = Acesso('user@gmail.com', '12345')
# print(user.email)
# AttributeError
# print(user.__senha)
# Conseguimos acessar - Chamamos de Name Mangling
# print(user._Acesso__senha)
print(user.get_email())
print(user.get_senha())
print(dir(user))

user1 = Acesso('diego.parente@hbsis.com.br', 'seishi22')
user2 = Acesso('diegohenrique.costa@gmail.com', '123456')

print(user1.get_email())
print(user2.get_email())


# Atributos de Classe
# São atributos que são declarados diretamente da classe, ou seja, fora do construtor, já inicializamos um valor, e este
# este valor é compartilhado entre todas as instâncias da classe, ou seja ao invés de cada instância ter os seus
# próprios valores com é o caso dos atributos de instância, os atributos de classe terão os mesmos valores
# - Não precisamos criar uma instância da classe para acessar o atributo de classe
class Produto:

    # Atributo de classe
    # 0.05% de imposto
    imposto = 1.05
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

print(f'O produto id {p1.id} {p1.nome} custa {p1.valor}')
print(f'O produto id {p2.id} {p2.nome} custa {p2.valor}')
# Forma correta para acessar o atributo de classe
print(f'Imposto é {Produto.imposto}')

# Atributos Dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução
# - O atributo criado será exclusivo da instância que o criou.
p1 = Produto('Playstation 4', 'Video Game', 2300)
p2 = Produto('Arroz', 'Marcearia', 5.99)
# Note que na classe Produto não existe o atributo 'peso'
p2.peso = '5kg'
print(f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor} e Peso: {p2.peso}')

# Deletando atributos dinamicos
print(p1.__dict__)
print(p2.__dict__)
del p2.peso
print(p1.__dict__)
print(p2.__dict__)
