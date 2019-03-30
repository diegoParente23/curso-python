"""
Módulos Externos

- Utilizamos o gerenciador de pacotes chamado de Pip - Python Installer Package.
- Os pacotes contidos em pip está no site
    - https://pypi.org

- colorama -> É utilizado para permitir impressão de textos coloridos no terminal.

Exemplos
from colorama import init
from colorama import Fore, Back, Style

init()
print(Fore.RED + 'Geek University')
print(Fore.BLUE + 'Geek University')
print(Fore.GREEN + 'Geek University')

print(Style.DIM + 'Geek University')
print(Back.BLUE + 'Geek University')
print(Back.RED + 'Geek University')
"""
import pydf

pdf = pydf.generate_pdf('<h1>Geek University</h1><br/><strong>Progrmação em Python: Essencial</strong>')

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
