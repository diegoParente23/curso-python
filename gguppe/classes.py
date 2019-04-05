"""
POO -> Classes

- Nada mais são do que modelos dos objetos do mundo real sendo representados computacionalmente

- Classes possuem:
    - Atributos -> Representam caracteristicas do objeto.
    - Métodos -> Comportamentos dos objetos (funções), ou seja, as ações que eles podem realizar dentro do sistema.

- Em python utilizamos a palavra reservada 'class' para definir a classe
- Utilizamos a palavras 'pass' em Python quando temos um bloco de código que ainda não está implementado.
- Quando nomeamos a nossa classe em python, utilizamos por convenção o nome com inical em maiusculo, se o nome for
composto utiliza-se as iniciais de ambas as palavras em maiusculo todas juntas.
- Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos estes
objetos que serão mapeados para classes de entidades.
"""


class Lampada:
    pass


# Exemplo de classe com nome composto
class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass


lamp = Lampada()
print(type(lamp))
