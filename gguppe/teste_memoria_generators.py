"""
Teste de memória com Generators

"""
# Fibonacci
# Função usandos listas


def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums


# Test1 449MB (100000)
for n in fib_lista(100):
    print(n)

# Função usando generators


def fib_gen(max):
    a, b, contador = 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1


# Test2 2.8MB (100000)
for n in fib_gen(100):
    print(n)
