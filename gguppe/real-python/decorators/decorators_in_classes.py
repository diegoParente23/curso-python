import functools
import time
import math
import random
from dataclasses import dataclass

# Decorators ----------------------------------------------------------------------

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

# Decorator with arguments --------------------------------------------------------

def repeat(_func=None, *,  num_times=1):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    
    if _func is None:
        return decorator_repeat
    
    return decorator_repeat(_func)

# Stateful Decorators -------------------------------------------------------------

def count_calls(func):
    @functools.wraps(func)
    def wrapper_cout_calls(*args, **kwargs):
        wrapper_cout_calls.num_calls += 1
        print(f"Call {wrapper_cout_calls.num_calls} of {func.__name__!r}")

        return func(*args, **kwargs)
    
    wrapper_cout_calls.num_calls = 0
    return wrapper_cout_calls

# Classes as Decorator ------------------------------------------------------------

class Counter(object):
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.count = 0
        self.func = func
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call {self.count} of {self.func.__name__!r}")

        return self.func(*args, **kwargs)

# ---------------------------------------------------------------------------------

# Classes -------------------------------------------------------------------------

@timer
class TimeWaster(object):
    # @debug
    def __init__(self, max_num):
        self.max_num = max_num
    
    # @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([i**2 for i in range(num_times)])


class PlayingCard(object):
    rank: str
    suit: str


# Nesting Decorators --------------------------------------------------------------

@debug
@timer
def greet(name):
    print(f"Hello {name}")

# ---------------------------------------------------------------------------------

@repeat(num_times=4)
def greet_v2(name):
    print(f"Hello! {name}")

@repeat
def say_good_morning(name):
    print(f"Good Morning {name}")
    
@count_calls
def say_whee():
    print("Whee!")


@Counter
def say_whee_v2():
    print("Whee!")

#----------------------------------------------------------------------------------

# Examples ------------------------------------------------------------------------

# tw = TimeWaster(1000)
# tw.waste_time(999)

# greet("Diego")

# greet_v2("Henrique")
# say_good_morning("Parente")

# say_whee()
# say_whee()

say_whee_v2()
say_whee_v2()

print(say_whee_v2.count)

# ---------------------------------------------------------------------------------
