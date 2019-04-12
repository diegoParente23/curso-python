#!/usr/bin/python
# -*- coding: iso-8859-15 -*
"""
Métodos de data e horas

https://docs.python.org/3/library/datetime.html

# Encontrar o dia da semana weekday()
# Os dias da semana no método weekday começam com 0, sendo 0 segunda feira
# 0 -> Monday
# 1 -> Tuesday
# 2 -> Wednesday
# 3 -> Thursday
# 4 -> Friday
# 5 -> Saturday
# 6 -> Sunday
print(manutencao.weekday())
weekdays = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}

aniversario = input('Qual é a sua data de nascimento? ')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))
print(f'Você nasceu em uma {weekdays[aniversario.weekday()]}')

# Formatando datas com strftime() (String Format time)
# dd/mm/yyyy hh:mm
months = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro',
}


def formata_data(data):
    return f'{data.day} de {months[data.month]} de {data.year}'


hoje = datetime.datetime.today()
print(hoje)
print()

print(hoje.strftime('%B'))
print(hoje.strftime('%d/%m/%Y'))
print(hoje.strftime('%d/%m/%y'))
print(hoje.strftime('%d/%B/%Y'))
print(hoje.strftime('%d/%b/%Y'))
print(hoje.strftime('%d de %b de %Y'))
print(formata_data(hoje))
"""
import datetime
import timeit, functools
from textblob import TextBlob

# Com o now podemos especificar um timezone (fuso horário)
agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))
print()

hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))
print()

# Mudanças ocorrendo à meia-noite combine()
# Agendando para o dia seguinte a meia-noite
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)
print()


def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(to='pt-br')} de {data.year}"


hoje = datetime.datetime.today()
print(hoje)
print()

print(hoje.strftime('%B'))
print(hoje.strftime('%d/%m/%Y'))
print(hoje.strftime('%d/%m/%y'))
print(hoje.strftime('%d/%B/%Y'))
print(hoje.strftime('%d/%b/%Y'))
print(hoje.strftime('%d de %b de %Y'))
# print(formata_data(hoje))

# Transformando uma string em datetime
nascimento = datetime.datetime.strptime('10/04/2008', '%d/%M/%Y')
nascimento = datetime.datetime.strptime('10/4/2008', '%d/%m/%Y')
print(nascimento)

# Somente hora
almoco = datetime.time(12, 40, 0)
print(almoco)

# Marcando tempo de execução do nosso método com timeit
# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

# List Comprhension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

# List Comprhension
tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(teste(5))
print(timeit.timeit(functools.partial(teste, 2), number=10000))
