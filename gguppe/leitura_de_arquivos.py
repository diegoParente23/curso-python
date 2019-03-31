"""
Leituras de Arquivos

Para ler arquivos em python, utilizamos a função integrada open().
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas um paramêtro de entrada, que no caso é o nome do
arquivo lido, esta função retorna um _io.TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão a função opne() abre o arquivo para leitura, Este arquivo deve existir, ou teremos o erro de
FileNotFoundError

<_io.TextIOWrapper name='text.txt' mode='r' encoding='cp1252'>

mode r -> Modo de leitura. r-> read() -> ler.
"""
# Exemplo:

arquivo = open('text.txt')
print(arquivo)
print(type(arquivo))

ret = arquivo.read()
print(ret)

# Para ler o conteúdo de um arquivo, após sua abertura, devemos utilizar a função read()
print(arquivo.read())

# OBS: O python utiliza um recurso para trabalhar com arquivos chamado cursor. Esse cursor funciona como o cursor
# quando estamos escrevendo.

# OBS: A função read() irá ler todo o conteúdo do arquivo.
