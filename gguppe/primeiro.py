
def funcao1():
    print('Geek University - primeiro.py')


if __name__ == '__main__':
    funcao1()
    print('Está sendo executado diretamente')
else:
    print(f'Está sendo importado {__name__}')
