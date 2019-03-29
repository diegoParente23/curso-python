"""
Debuggando com PDB

PDB -> Python Debugger

Vida de Inseto -> Life's Bug

Bug -> Inseto

- Utilizar o print para debugar é uma prática ruim, existem formas mais profissionais de se fazer, exemplo o 'Debugger'
pode ser utilizado em diferentes IDE's
- Para utilizar o python debugger, precisamos importar o pacote pdb e então utilizar a função set_trace()
- Por que utilizar o PDB ?
    - Custommanos realizar todos os imports no início do arquivo, Por isso ao invés de colocar o import pdb no ínicio
    do arquivo, nós colocamos somente somente onde vamos debuggar
- A partir do python 3.7 não é mais preciso importar o pacote pdb, pois a mesma já faz parte como uma função built-in
da linguagem atrávez do breakpoint()
- OBS C U I D A D O
    - Com conflitos entre nomes de variáveis e os comandos do pdb
    - Se os nomes das variáveis forem os mesmos dos comandos, utilizar a letra p para imprimir os valores
    - Evite colocar nomes não representativos para variáveis, optar por nomes significativos

# Exemplo com PhyCharm
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema \n Error: {err}'


print(dividir(4, 7))

print()

# Exemplo com PDB
# Comando básicos
# l (para listar onde estamos no código)
# n (próxima linha)
# p (imprime variável)
# c (continua a exceção - finaliza o debugging)
import  pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o cuso ' + curso

# Exemplo PDB 2
import pdb; nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o cuso ' + curso
"""
nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' faz o cuso ' + curso

