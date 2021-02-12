from time import perf_counter
import functools


def timed(func):
    @functools.wraps(func)
    def wrapper_timed(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        print(perf_counter() - start)
        return result

    return wrapper_timed
