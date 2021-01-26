class C:
    pass


def func():
    pass

obj = C()
print(sorted(set(dir(func)) - set(dir(obj))))
