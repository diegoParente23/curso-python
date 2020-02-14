
colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# Cartesian Product with list comprehensions

tshirts = [(size, color) for size in sizes for color in colors]

# [('S', 'black'), ('S', 'white'), ('M', 'black'), ('M', 'white'), ('L', 'black'), ('L', 'white')]
print(tshirts)

for color in colors:
    for size in sizes:
        print((color, size))

tshirts = [(color, size) for size in sizes for color in colors]

# [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
print(tshirts)

for tshirts in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirts)
