import functools
import time
import math


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


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


# Slowing down code: you could be troubleshooting an api accessing information
# over a network or maybe you simply need to put a function into wait state
def slow_down(func):
    """Sleep 1 second before calling the function."""
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return wrapper_slow_down


# Stateful decorator
def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f'Call {wrapper_count_calls.num_calls} of {func.__name__!r}')
        return func(*args, **kwargs)

    # These are called function attributes, couldn't find much information
    # about this, refer: https://stackoverflow.com/questions/338101/python-function-attributes-uses-and-abuses
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls
