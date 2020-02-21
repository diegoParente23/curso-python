#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

lista = [10, 20, 30, 40, 50, 60]

print(lista[:2])  # começa a partir do primeiro indice e vai até o terceiro
print(lista[2:])  # começa a partir do terceiro indice e vai até o final do array

s = 'bicycle'
print(s[::3])
print(s[::-1])
print(s[::-2])
print()

invoice = """
0......6..................................40........52...55........
1909   Pimoroni PiBrella                      $17,50    3    $52,50
1489   6mm Tactile Switch x20                 $4,95     2     $9,50
1510   Panavise Jr. - PV-201                  $28,00    1    $28,00
1601   PiTFT Mini Kit 320x240                 $34,95    1    $34,95
"""

SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
UNIT_PRICE = slice(40, 52)
QUANTITY = slice(52, 55)
ITEM_TOTAL = slice(55, None)

line_items = invoice.split('\n')[2:]

for item in line_items:
    print(item[UNIT_PRICE], item[DESCRIPTION])
