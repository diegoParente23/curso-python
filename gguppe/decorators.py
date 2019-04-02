"""
Decoradores (Decorators)

- Decorators são funções
- Decorators envolvem outras funções e aprimoram seus comportamentos.
- Decorators são exemplos de Higher Order Functions;
- Decorators tem uma sintax própria, usando "@" (Syntact Sugar / Açucar Sintático)
"""

# Decorators como funções (Sintax não recomendado / Sem açucar sintático)


def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja Bem-vindo(a) à Geek University')


# Testando 1
teste = seja_educado(saudacao)
teste()

# Testando 2


def raiva():
    print('EU TE ODEIO')


raiva_educada = seja_educado(raiva)
raiva_educada()


# Decorators com Syntax Sugar (Açucar Sintático)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Pedro')


# Testando
apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')


dormir()


# OBS: Não confunda decorator function, com decorator
