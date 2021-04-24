from functools import wraps
from time import perf_counter


def timeit(func):
    """Print the runtime of the decorated function"""
    @wraps(func)
    def wrapper_timeit(*args, **kwargs):
        beg = perf_counter()
        res = func(*args, **kwargs)
        end = perf_counter()
        run = end - beg
        print(f'inp: {unpack_list(args)}{unpack_dict(kwargs)}\n'
              f'out: {res}\n'
              f'Function {func.__name__!r} took {run:.10f} secs\n')
        return res

    return wrapper_timeit


def unpack_list(data: list) -> str:
    return ' '.join(f'{item}' for item in data)


def unpack_dict(data: dict) -> str:
    return ' '.join(f'{key}={val}' for key, val in data.items())
