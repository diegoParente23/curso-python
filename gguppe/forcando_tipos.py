"""
Forçando tipos de dados com decorators

"""
# Python não precisamos definir o tipo de dado
numero = 10
texto = 'Diego'
booleano = True


def forca_tipo(*tipos):
    def decorador(funcao):
        def converter(*args, **kwargs):
            novo_args = []
            for(valor, tipo) in zip(args, tipos):
                novo_args.append(tipo(valor))
            return funcao(*novo_args, **kwargs)
        return converter
    return decorador


@forca_tipo(str, int)
def repete_msg(msg, vezes):
    for vez in range(vezes):
        print(msg)


repete_msg('Geek', '3')


@forca_tipo(float, float)
def dividir(a, b):
    print(a/b)


dividir(3.45, 1.23)
dividir(3.45, 5)

