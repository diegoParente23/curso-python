"""
Módulos Customizados

Como módulos python nada mais são de que arquivos python, todos os arquivos que criamos neste cursos são módulos
python prontos para serem utilizados.

# from modulo_somar_pares import somar_impares as fcp
import modulo_somar_pares as fcp

print(fcp.somar_impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(fcp.somar_impares(fcp.lista))
print(fcp.lista)
"""
from map import cidades, c_para_f

print(list(map(c_para_f, cidades)))
