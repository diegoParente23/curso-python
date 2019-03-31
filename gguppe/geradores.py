"""
Geradores

- Generators -> São iterators (Iteradores)

OBS: O contrário não é verdadeiro, ou sej, nem todo iterator é um generator.

- Outras informações:
    - Generators podem ser criados com funções geradoras.
    - Funções geradoras utilizam a palavra reservada yield.
    - Generators podem ser criados com Expressões Geradoras

- Diferenças entre funções e generator functions (Funções geradoras)

------------------------------------------------------------------------------------
| Funções                            | Generator Functions                          |
------------------------------------------------------------------------------------
| Utilizam return                    | Utilizam yield                               |
------------------------------------------------------------------------------------
| Retorna uma vez                    | Podem utilizar yield multiplas vezes         |
-------------------------------------------------------------------------------------
| quando executada, retorna um valor | quando executada retorna um generator        |
-------------------------------------------------------------------------------------

# Exemplos

gen = conta_ate(5)
print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = conta_ate(10)
for n in gen:
    print(n)
"""
# Exemplo Generator Function
# OBS: Uma generator function não é um generator, ela gera um generator


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1


gen = conta_ate(10)
print(next(gen))
print()
for n in gen:
    print(n)

print()

lista = list(conta_ate(20))
for n in lista:
    print(n)
