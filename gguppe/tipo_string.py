"""
Tipo string
"""

nome = 'Diego'
nome = "DIEGO"
nome = '''Dih'''
nome = """DiDi"""

print(nome)
print(nome.upper())
print(nome.lower())
print(nome.replace("D", "X"))
print(type(nome))

nome = "Gina's Bar"

print(nome)

nome = 'Angelina \n Jolie'
nome = """ Angelina
Jolie"""

print(nome)
print(nome.split())
print(nome.split()[1])

# Similar ao substring do C#
# Slice de string
var = nome[0:4]
print(var)

# Inversão da string
# [::-1} -> Comece do primeiro elemento, vá até o último elemento e inverta
print(nome[::-1])

texto = 'socorram me subino onibus em marrocos'

print(texto)
print(texto[::-1])
