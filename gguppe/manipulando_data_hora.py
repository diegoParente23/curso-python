#!/usr/bin/python
# -*- coding: iso-8859-15 -*
"""
Manipulando data e hoera

datetime
"""
import datetime

# print(dir(datetime))
print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# 2019-04-11 21:21:37.662264
print(datetime.datetime.now())

# datetime.datetime(2019, 4, 11, 21, 23, 53, 543226)
print(repr(datetime.datetime.now()))

# replace() para fazer ajustes
inicio = datetime.datetime.now()
print(inicio)

# Alterar o horario para 16 horas, 0 minutos, 0 segundos, 0 microsegundos.
inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)
print(inicio)

# Criar data e hora
evento = datetime.datetime(year=2019, day=1, month=1)
print(evento)

# Exemplo mais dificil
nascimento = input('Qual a sua data de aniversário ? (dd/mm/yyyy) ')
nascimento = nascimento.split('/')
nascimento = datetime.datetime(year=int(nascimento[2]), month=int(nascimento[1]), day=int(nascimento[0]))
print(nascimento)
print(type(nascimento))

print()

# Acesso individual dos elementos de data e hora.
evento = datetime.datetime.now()
print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)
