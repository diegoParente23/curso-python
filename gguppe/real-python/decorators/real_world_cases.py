import functools
import time
import math
import random

# ---------------- Decorators -------------------------------------

# Timing Functions ------------------------------------------------

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time

        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    
    return wrapper_timer

# Debugging Code ---------------------------------------------------

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)

        print(f"Calling {func.__name__}({signature})")

        value = func(*args, **kwargs)

        print(f"{func.__name__!r} returned {value!r}")

        return value

    return wrapper_debug


# Slowing Down Code ------------------------------------------------

def slow_down(func):
    """Sleep 1 second before calling the function"""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    
    return wrapper_slow_down

# Registering Plugins ----------------------------------------------

PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

#-------------------------------------------------------------------

# ---------------- Examples ----------------------------------------

@timer
def waste_some_time(num_times: int):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


@slow_down
def count_down(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        count_down(from_number -1)


# make_greeting(name="Diego", age=29)


math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


# print(approximate_e(5))

# count_down(3)

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)


print(PLUGINS)
print(randomly_greet("Alice"))
