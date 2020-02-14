#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import array

symbols = '$€¥£'

# Fisrt form - Commom

codes = []

for symbol in symbols:
    codes.append(ord(symbol))

print(codes)

# Second form - List comprehensions

codes = [ord(symbol) for symbol in symbols]

print(codes)

# Comparism between listcomps vs map/filter

beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]

print(beyond_ascii)

beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))

print(beyond_ascii)

# Generation expression

codes = tuple(ord(symbol) for symbol in symbols)

print(codes)

codes = array.array('I', (ord(symbol) for symbol in symbols))

print(codes)
