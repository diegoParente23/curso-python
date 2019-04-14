"""
Introdução ao módulo Unittest

- Teste unitários
- O que são ?
    - É a forma de se testar unidades individuais de codigo fonte.
    - Podem ser, funções, métodos, classes e etc.

# OBS: Testes unitários não é especifico da linguagem Python.

Para criar nossos testes criamos classes que herdam da classes do Unittests. TestCase
e a partir daí ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos o unittests.main().

https://docs.python.org/3/library/unittest.html

# Conhecendo os assertions

Método                   Checa que
assertEqual(a, b)        a == b
assertNotEqual(a, b)     a != b
assertTrue(x)            x é verdadeiro
assertFalse(x)           x é false
...

# Por convenção todos os testes em um test case, devem ter o seu nome iniciado com test_
# Para exceutar os testes com o unittests, use
    - python file.py
# Para executar os testes com unittests no modo verbose (com detalhes do que está acontecendo).
    - python file.py -v

# Docstrings nos testes
    - Podemos e devemos inserir docstrings nos testes (Super recomendado).
"""
# Prática - Utilizando abordagem
