"""
Introdu��o ao m�dulo Unittest

- Teste unit�rios
- O que s�o ?
    - � a forma de se testar unidades individuais de codigo fonte.
    - Podem ser, fun��es, m�todos, classes e etc.

# OBS: Testes unit�rios n�o � especifico da linguagem Python.

Para criar nossos testes criamos classes que herdam da classes do Unittests. TestCase
e a partir da� ganhamos todos os 'assertions' presentes no m�dulo.

Para rodar os testes, utilizamos o unittests.main().

https://docs.python.org/3/library/unittest.html

# Conhecendo os assertions

M�todo                   Checa que
assertEqual(a, b)        a == b
assertNotEqual(a, b)     a != b
assertTrue(x)            x � verdadeiro
assertFalse(x)           x � false
...

# Por conven��o todos os testes em um test case, devem ter o seu nome iniciado com test_
# Para exceutar os testes com o unittests, use
    - python file.py
# Para executar os testes com unittests no modo verbose (com detalhes do que est� acontecendo).
    - python file.py -v

# Docstrings nos testes
    - Podemos e devemos inserir docstrings nos testes (Super recomendado).
"""
# Pr�tica - Utilizando abordagem
