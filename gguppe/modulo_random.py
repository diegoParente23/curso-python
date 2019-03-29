"""
Módulo Random

O que são módulos ?
- Nada mais são do que outros arquivos python
- Util para deixar o código mais simple e serve para reaproveitar código
- Os módulos podem ser compartilhados com a comunidade

random()
    - Possui várias funções que geram números pseudo-aleatório (os números podem repetir) entre 0 e 1

# OBS Existem duas formas de se utilizar um módulo ou função
# Forma 1 - N Ã O  R E C O M E N D A D O
# Importando todo o módulo
# Ao realizar o import completo, todos os métodos, funções e atributos e classes que estiverem dentro deste módulo
# ficara disponível (Em memória)
import random
print(random.random())

# Veja que para utilizar a função random do módulo random, nós colocamos o nome do pacote e o nome da função.
# separados por '.'
# Não confunda a função 'random()' com o módulo 'random', a função 'random()' é apenas uma função do módulo random

# Forma 2 - Importando uma função especifica do módulo
# R E C O M E N E D A D O
from random import random

# No import acima estamos falando do módulo random import a função random

# Exemplo de uso
for i in range(10):
    print(f'{random()}')
"""
# uniform() -> Gerar números pseudo-aleatórios entre os valores estabelecidos
from random import uniform

# o valor '7' não é incluido
for i in range(10):
    print(uniform(3, 7))

# randint() -> Gera valores inteiros pseudo-aleatórios entre os valores estabelecidos
from random import randint

print()

# Gerador de apostas para a mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')

print()

# choice() -> Mostra um valor aleatório entre um iterável
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))
print(choice('DIEGO HENRIQUE COSTA PARENTE'))

# shuffle() -> Tem a função de embaralhar dados
from random import shuffle
cartas = ['K', 'Q', 'J', 'A', 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(cartas)
shuffle(cartas)
print(cartas)
print(cartas.pop())
