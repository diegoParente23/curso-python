"""
Erros mais comuns

- A T E N Ç Ã O
Importante prestar a atenção e ler as saídas de erros de excução do código

- SintaxeError -> Ocorre quando o Python encontra um erro de sintaxe, ou seja você escreveu algo que o Python não
reconhece como parte da linguagem.

a)
    def funcao:
        print('Geek')

b) Palavra reservada
    def = 1

c)
    return

- NameError -> Ocorre quando uma variável ou função não foi definida

a) Variável geek não foi definida
    print(geek)

b) método geek() não foi definido
    geek()

c) Se o 'a' for maior que 10 não será criado a variável 'msg'
    a = 8
    if a < 10:
        msg = 'É maior que 10'
    print(msg)

- TypeError -> Ocorre quando uma função/operação/ação é aplicada a um tipo errado.

a) O método len somente pode ser usado em tipos iteráveis
    print(len(5))

b) Não é possivel concatenar uma string a um array vazio.
    print('Geek' + [])

- IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado utilizando
um indice inválido.

a) A lista tem somente um registro
    lista = ['Geek']
    print(list[1])

- ValueError -> Ocorre quando uma função/operação built-in (integrado) recebe um argumento com tipo correto mas valor
inapropriado.

a) O 'int()' espera um tipo string porém com um número
    print(int('Geek'))

b) O 'float()' espera um tipo string porém com um número
    print(float('a'))

- KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe

a) A chave 'b' não existe no dicionário
    dicionario = { 'a': 1 }
    print(dicionario['b']

- AttribuiteError -> Ocorre quando uma variável não tem um atributo ou função

a) O método 'sort' não existe em tuple, somente em list
    tupla = (11, 2, 31, 4)
    tupla.sort()

- IndentationError -> Ocorre quando o código não está identado corretamente

a) O método 'print()' deve estar com quatro espaços de identação.
    a = 10
    if a < 10:
    print(a)
"""

