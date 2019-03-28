"""
Try Except -> Utilizamos o bloco try except para tratar erros que podem ocorrer no nosso código. Previnindo assim que
o programa pare de funcionar e o usuário receba mensagens de erros inesperados.

A forma geral mais simples
try:
    // Execução problemática
except:
    // O que deve ocorrer para tratar o problema
"""
# Exemplo 1 - Tratando um erro genérico
# OBS: Tratar erros de formas genéricas não é a forma ideal para se tratar
# O melhor é tratar erros específicos.
try:
    geek()
except:
    print('Deu ruim aqui')

print()

try:
    geek()
except NameError as err:
    print(f'Deu ruim aqui \nError: {err}')

print()

try:
    print('Geek'[9])
except NameError as err:
    print(f'Deu ruim \n{err}')
except TypeError as err:
    print(f'Deu ruim \n{err}')
except:
    print(f'Erro não mapeado')


def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None


dic = {'x': 'Diego'}
print(pega_valor(dic, 'nome'))
