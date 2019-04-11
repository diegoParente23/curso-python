"""
JSON e Pickle

JSON - Javascript Object Notation

# Integrando o json com pickles
# pip install jsonpickle
import jsonpickle

ret = jsonpickle.encode(felix)
print(ret)
"""
import json

ret = json.dumps(['produtos', {'Playstation 4': ('2TB', 'Novo', '220V', 2340)}])
print(type(ret))
print(ret)


class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @property
    def raca(self):
        return self.__raca


felix = Gato('Felix', 'Vira-Lata')
ret = json.dumps(felix.__dict__)
print(ret)

# Integrando o json com pickles
# pip install jsonpickle
import jsonpickle

# Escrevendo o json no pickle
with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)

# Lendo o json do pickle
with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(ret.nome)
    print(ret.raca)
