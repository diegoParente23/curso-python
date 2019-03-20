"""
Entendendo *args

- O *args é como outro parametro qualquer, isso significa que você poderá chamar de qualquer coisa
desde que comece com *

Exemplo

*xis

Mas por conveção, utilizamos *args para defini-lo

- O args não consegue receber listas, pois ele trata como um único argumento
"""
# Exemplos


def soma_todos_os_numero(*args):
    return sum(args)


print(soma_todos_os_numero())
print(soma_todos_os_numero(1))
print(soma_todos_os_numero(1, 2))
print(soma_todos_os_numero(1, 2, 3))
print(soma_todos_os_numero(1, 2, 3, 4))
print(soma_todos_os_numero(1.20, 2.99, 3.87, 4.34))


def outra(nome, email, *args):
    print(f'Sr {nome}, de email {email}, o total foi {sum(args)}')


print(outra('Diego', 'diego.parente@contato.com', 2, 4, 5, 6))


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek'
    return 'Eu não tenho certeza de que é você...'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))


numeros = [1, 2, 3, 4, 5, 6]

# O * serve para informarmos ao python que estamos passando como argumentos uma coleção de dados, desta forma
# ele saberá o que precisará antes de desempacotar os dados.
print(soma_todos_os_numero(*numeros))
