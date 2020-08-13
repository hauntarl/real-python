import random
import math
import functools
import time


def decorator(func):
    """template or boilerplate to write your decorators."""
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before running your function
        value = func(*args, **kwargs)
        # Do something after
        return value

    return wrapper_decorator


# Timing functions with decorators
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # 1

        value = func(*args, **kwargs)

        end_time = time.perf_counter()  # 2
        run_time = end_time - start_time
        print(f'Finished {func.__name__!r} in {run_time:.4f} secs')
        return value

    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i ** 2 for i in range(10000)])


waste_some_time(1)
waste_some_time(100)


# Debugging code with decorators
def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})')

        value = func(*args, **kwargs)

        print(f'{func.__name__} returned {value!r}')
        return value

    return wrapper_debug


@debug
def make_greeting(name, age=None):
    if age is None:
        return f'Howdy {name}!'
    return f'Whoa {name}! {age} already, you are growing up!'


print()
make_greeting('Benjamin')
make_greeting('Richard', age=112)
# this might not seem as much, since the decorator is simply repeating what you
# wrote. But it is suggested that you use it on a more complex function. There
# is another advance way to use it. Its actually more powerful when you apply it
# to a small convenience functions that you didn't directly call yourself.


# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


print()
print(approximate_e(5))


# Slowing down code: you could be troubleshooting an api accessing information
# over a network or maybe you simply need to put a function into wait state
def slow_down(func):
    """Sleep 1 second before calling the function."""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return wrapper_slow_down


@slow_down
def count_down(from_number):
    if from_number < 1:
        print('Lift Off!')
        return
    print(from_number)
    count_down(from_number - 1)


print()
count_down(3)


# Registering Plugins using decorators:
PLUGINS = {}


def register(func):
    """Register a function as a plugin"""
    PLUGINS[func.__name__] = func
    return func


@register
def say_hello(name):
    return f'Hello {name}'


@register
def be_awesome(name):
    return f'Yo {name}, together we are the awesomest!'


print()
print(PLUGINS)


def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f'Using {greeter}')
    return greeter_func(name)


print()
print(randomly_greet('Alice'))

# the main benefit of this simple architecture is that you don't have to
# maintain a list of which plugins exists, the list gets created each time you
# apply decorator to functions.
