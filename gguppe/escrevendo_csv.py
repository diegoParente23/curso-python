"""
Escrevendo CSV

writer() -> Gera um objeto que possamos escrever em um arquivo csv
writerow() -> Escreve uma linha, esse método recebe uma lista

# writer()
from csv import writer

with open('filmes.csv', 'w') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Titulo', 'Genero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o genêro: ')
            duracao = input('Informe a duração(em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])
"""
# DictWriter
from csv import DictWriter

with open('filmes2.csv', 'w') as arquivo:
    cabecalho = ['Título', 'Genêro', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o genêro: ')
            duracao = input('Informe a duração(em minutos): ')
            escritor_csv.writerow({'Título': filme, 'Genêro': genero, 'Duração': duracao})
