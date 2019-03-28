"""
Try - Except - Else - Finally

Dica de quando e onde tratar erro no código

TODA A ENTRADA DO USUÁRIO DEVE SER TRATADAS!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'
"""
# Else -> É executado somente se não ocorrer o erro.
# Finally -> Sempre é executado ocorrendo ou não erro.
# Geralmente é utilizado para fechar ou desalocar recursos.
num = 0
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')
finally:
    print('Método finalizado')

# Exemplo mais complexo


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema \n Error: {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))
