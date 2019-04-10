"""
POO - Métodos Mágicos

- São todos os métodos que usam dunder, quando utilizam double underscore

dunder init -> __init__()
dunder repr -> __repr__() Representação do objeto (ToString() do C#)
dunder str -> __str__() Transforma o objeo em string
"""


class Livro:

    def __init__(self, titulo, autor, paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    def __repr__(self):
        return f'{self.__titulo} escrito por {self.__autor}'

    def __str__(self):
        return self.__titulo

    def __len__(self):
        return self.__paginas

    def __del__(self):
        print(f'Um objeto do tipo {type(self)} foi deletado da memória')

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)
livro3 = Livro('Harry Potter', 'Geek', 700)
print(livro1)
print(livro2)
print(len(livro1))
del livro1
print(livro2 + livro3)
print(livro2 * 3)
