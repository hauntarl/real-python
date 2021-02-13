from time import perf_counter
import functools


def timed(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = perf_counter()  # 1
        result = func(*args, **kwargs)
        end_time = perf_counter()  # 2
        run_time = end_time - start_time
        print(f'Finished {func.__name__!r} in {run_time:.10f} secs')
        return result

    return wrapper_timer
