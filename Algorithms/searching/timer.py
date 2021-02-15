import functools

from time import perf_counter


def timed(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timed(*args, **kwargs):
        beg = perf_counter()  # 1
        res = func(*args, **kwargs)
        end = perf_counter()  # 2
        run = end - beg
        print(f'Finished {func.__name__!r} in {run:.10f} secs')
        return res

    return wrapper_timed
