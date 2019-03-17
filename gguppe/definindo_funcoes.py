"""
Definindo Funções

- Funções são pequenos trechos de código que realizam tarefas especificas:
- Podem ou não receber entrada/saída de dados
- Úteis para executar procedimentos similares por repetidas vezes

OBS: Se você escrever uma função que realiza várias tarefas dentro delas,
é bom fazer uma verificação para que a função seja simplificada.

- Exemplos de utilização
    - print()
    - len()
    - min()
    - max()
    - count()

- Dry - Don't repeat yourself - Não repita você mesmo/código

Forma geral de definir função

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

- def -> Para definir uma função
- nome_da_funcao -> SEMPRE, com letras minusculas e se for nome composto, separado por underline (Snake Case);
- parametros_de_entrada -> Opcionais, onde tendo mais de um cada um separado por virgula, podendo ser opcional ou não
- bloco_da_funcao -> processamento da função

OBS: para definir função usar o def
"""
# Exemplo de utilização de função

cores = ['verde', 'amarelo', 'azul', 'vermelho']
print(cores)

curso = 'Programação em Python Essencial'
print(curso)

cores.append('roxo')
print(cores)

# Como definir funções


# 1° Função
def diz_oi():
    print('Oi')


# Chamada de execução da função
diz_oi()


# Exemplo 2
def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva ao aniversariante')


print()

for n in range(1, 5):
    print(f'{n} vez')
    cantar_parabens()
    print()


# Podemos criar variáveis do tipo da função para executar esta função atrávez da variável
canta = cantar_parabens

canta()


