"""
Dunder Name e Dunder Main

Dunder -> double under ('__')

Dunder Name -> __name__
Dunder Main -> __main__

- Em Python são utilizados dunder para criar funções, atributos, propriedades e etc. Utilizando Double Under para não
gerar conflito com os nomes desses elementos na programação

Em C

int main() {
}

Em Java

public static void main(String[] args) {
}

Em Python: se executarmos um módulo python diretamente na linha de comando, internamente o Python atribuirá __name__
o valor __main__ indicando que este módulo é o módulo de execução principal.
"""
from funcoes_com_parametros import somar_impares
import primeiro
import segundo

print(somar_impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
