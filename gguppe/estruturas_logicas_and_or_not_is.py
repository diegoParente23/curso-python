"""
Estruturas lógicas

and(e), or(ou), not(não) e is(é)
"""

ativo = False
logado = True

if ativo and logado:
    print('Bem vindo usuário')
else:
    print('Você precisa ativar a sua conta por e-mail')

if ativo is False:
    print('Ativo é False')
else:
    print('Ativo é True')

if not logado:
    print('Você precisa estar logado')

if ativo:
    print('Bem vindo usuário')
