"""
Documentando funções com Doc Strings

- Podemos ter acesso a documentação de uma função em python utilizando a propriedade especial
__doc__
"""
# Exemplos


def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi'


def exponencial(numero, exponecia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'número' à 'potêncial' informada.
    :param numero: Número que desejamos gerar o exponencial
    :param exponecia: Potêncial que desejamos gerar o exponencial, Por padrão é 2
    :return: Retorna o exponêncial de 'número' por 'potência'
    """
    return numero ** exponecia


print(9)
