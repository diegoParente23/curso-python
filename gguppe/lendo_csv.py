"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores separados por virgula
    - ','
    - ';'
    - ' '

http://dados.gov.br/dataset

# Possível de se trabalhar porém não é o ideal (Trabalhoso)
with open('lutadores.csv') as arquivo:
    dados = arquivo.read().split(',')[2:]
    print(type(dados))
    print(dados)

- A Linguagem python possui duas formas diferentes para ler os dados em csv
    - reader -> Permite iterar sobre as linhas do arquivo como listas
    - DictReader -> Permite que iteremos sobre as linhas do arquivo csv como OrderedDicts;

# Reader
# Para colocar outro delimitador, basta passar um novo parametro
from csv import reader

with open('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    # Para pular o cabeçalho
    next(leitor_csv)
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a)(s) {linha[1]} e mede {linha[2]} centimetros')
"""
# DictReader
# Para colocar outro delimitador, basta passar um novo parametro
from csv import DictReader

with open('lutadores.csv') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a)(s) {linha['Pais']} e mede {linha['Altura (em cm)']} centimetros")
