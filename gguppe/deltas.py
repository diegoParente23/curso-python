#!/usr/bin/python
# -*- coding: iso-8859-15 -*
"""
Trabalhando com deltas de datas e horas (Diferença entre duas datas e horas)

data_inicial = dd/mm/yy 12:55:00.999
data_final = dd/mm/yy 13:55:00.999

delta = data_final - data_inicial
"""
import datetime

data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(2019, 5, 5, 0)
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))
print(tempo_para_evento)
print(tempo_para_evento.days)
# Duas barras para ignorar o ponto flutuante da conta.
print(f'Faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60} horas')

data_da_compra = datetime.datetime.now()
print(data_da_compra)

regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)

vencimento_boleto = data_da_compra + regra_boleto
print(vencimento_boleto)
