
# Introduction

# def add_one(number: int):
#     return number + 1


# def say_hello(name):
#     return f"Hello {name}"


# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"


# def greet_diego(greeter_func):
#     return greeter_func("Diego")


# def parent():
#     print("Printing from the parent() function")

#     def first_child():
#         print("Printing from the first_child() function")
    
#     def second_child():
#         print("Printing from the second_child() function")
    
#     second_child()
#     first_child()


# def parent_v2(num: int):
#     def first_child():
#         return "Hi, I am Emma"
    
#     def second_child():
#         return "Call me Liam"
    
#     if num == 1:
#         return first_child
#     else:
#         return second_child


# number = add_one(5)

# print(number)
# print(greet_diego(be_awesome))
# parent()

# print(parent_v2(1))
# print(parent_v2(2))

# Simple Decorator

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    
    return wrapper


def say_whee():
    print("Whee!")


say_whee = my_decorator(say_whee)
# say_whee()


from datetime import datetime


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass # Hush, the neighbors are asleep
    
    return wrapper


def say_whee_2():
    print("Whee!")


say_whee_2 = not_during_the_night(say_whee_2)
# say_whee_2()

# Syntax Sugar

@my_decorator
def say_whee_2():
    print("Whee!")

#say_whee()
