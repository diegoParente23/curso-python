
# Simple decorator

# def do_twice(func):
#     def wrapper_do_twice():
#         func()
#         func()
    
#     return wrapper_do_twice


# @do_twice
# def greet():
#     print("Hello Diego")


# greet()


# Decorator with parameters

# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
    
#     return wrapper_do_twice


# @do_twice
# def greet(name):
#     print(f"Hello {name}")


# greet("Diego")

# Returning Values From Decorated Functions

# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
    
#     return wrapper_do_twice


# @do_twice
# def returning_greet(name):
#     print("Creating greeting")
#     return f"Hi {name}"


# print(returning_greet("Diego"))

# Who Are You, Really ? use functools.wraps

import functools

def do_twice(func):
    
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    
    return wrapper_do_twice


@do_twice
def returning_greet(name):
    print("Creating greeting")
    return f"Hi {name}"

print(returning_greet.__name__)
