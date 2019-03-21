"""
**kwargs

- Chamamos de **kwargs
- Este é só um paramêtro, mas diferente do args que coloca valores extras em uma tupla,
o **kwargs exige que utilizemos paramêtros nomeados, e transforma esses paramêtros extras
em um dicionário
- Os paramêtros *args e **kwargs não são obrigatórios

Importante Podemos ter
- Paramêtros obrigatório
- *args
- Paramêtros não obrigatórios (default)
- **kwargs
"""
# Exemplos


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita do(a) {pessoa.title()} é {cor}')


cores_favoritas(diego='verde', julia='vermelho', mannuela='rosa')

# Exemplo mas complexo


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek!'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(diego='Python'))
print(cumprimento_especial(geek='C#'))


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(28, 'Diego Parente')
minha_funcao(28, 'Diego Parente', True, apelido='Dih')
minha_funcao(28, 'Diego Parente', 1, 2, 3, 4, solteiro=True, apelido='Dih')


def mostrar_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


# Desempacotar com **
nomes = {'nome': 'Diego', 'sobrenome': 'Jones'}
print(mostrar_nomes(**nomes))


def soma_multiplo_numeros(a, b, c, **kwargs):
    return a + b + c


print(soma_multiplo_numeros(1, 2, 3))
print(soma_multiplo_numeros(*[1, 2, 3]))
print(soma_multiplo_numeros(*(1, 2, 3)))
print(soma_multiplo_numeros(*{1, 2, 3}))
# OBS Os nomes das chaves devem ser iguais aos paramêtros da função
print(soma_multiplo_numeros(**dict(a=1, b=2, c=3, nome='Diego')))
