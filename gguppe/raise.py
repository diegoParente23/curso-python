"""
Raise -> Levantando os próprios erros

Lança exceções 'raise' é uma palavra reservada e não uma função, util para criar as próprias exceções e erros

Forma geral de uso:
    raise TipoDoErro('Mensagem de erro')

Exemplos:
    raise ValueError('Valor Incorreto')

- nada após o 'raise' não é executado, ou seja ele finaliza a função que está contido.
"""


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('O texto não é uma string')
    if type(cor) is not str:
        raise TypeError('A cor não é uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('Geek', 'verde')
colore('Geek', 'vermelho')
