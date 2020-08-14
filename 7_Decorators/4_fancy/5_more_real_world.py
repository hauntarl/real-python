"""
- Slowing Down Code, Revisited:

As noted earlier, our previous implementation of @slow_down always sleeps for 
one second. Now you know how to add parameters to decorators, so let’s rewrite 
@slow_down using an optional rate argument that controls how long it sleeps.
"""
import functools
import time

from decorators import timer, count_calls


def slow_down(_func=None, *, rate=1):
    """Sleep given amount of seconds before calling the function"""
    def decorated_slow_down(func):
        @functools.wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapper_slow_down

    return decorated_slow_down(_func) if _func else decorated_slow_down


@slow_down(rate=0.5)
def count_down(from_number):
    if from_number < 1:
        print('Lift Off!')
        return
    print(from_number)
    count_down(from_number-1)


count_down(3)


"""
- Creating Singletons:

A singleton is a class with only one instance. There are several singletons in 
Python that you use frequently, including None, True, and False. It is the fact 
that None is a singleton that allows you to compare for None using the is 
keyword, like you saw in the Both Please section.
"""


def singleton(cls):
    """Make a given class a singleton one"""
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None
    return wrapper_singleton
# As you see, this class decorator follows the same template as our function
# decorators. The only difference is that we are using cls instead of func as
# the parameter name to indicate that it is meant to be a class decorator.


@singleton
class Singleton:
    pass


first = Singleton()
second = Singleton()
print()
print(f'first == second? {first == second}')
print(f'first is second? {first is second}')
"""
Note: Singleton classes are not really used as often in Python as in other 
languages. The effect of a singleton is usually better implemented as a global 
variable in a module.
"""


"""
- Caching Return Values:

Decorators can provide a nice mechanism for caching and memoization. As an 
example, let’s look at a recursive definition of the Fibonacci sequence.
"""


@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


@timer
def call_fibonacci():
    fibonacci(10)


print()
call_fibonacci()
print(fibonacci.num_calls)
"""
NOTE: While the implementation is simple, its runtime performance is terrible.

To calculate the tenth Fibonacci number, you should really only need to 
calculate the preceding Fibonacci numbers, but this implementation somehow 
needs a whopping 177 calculations. It gets worse quickly: 21891 calculations 
are needed for fibonacci(20) and almost 2.7 million calculations for the 30th 
number. This is because the code keeps recalculating Fibonacci numbers that are 
already known.

The usual solution is to implement Fibonacci numbers using a for loop and a 
lookup table. However, simple caching of the calculations will also do the trick
"""


def cache(func):
    """Keeps a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        # Since a dictionary is used to cache results, the positional and
        # keyword arguments to the function must be hashable.
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]

    wrapper_cache.cache = {}
    return wrapper_cache


@cache
@count_calls
def cached_fibonacci(num):
    if num < 2:
        return num
    return cached_fibonacci(num - 1) + cached_fibonacci(num - 2)


@timer
def call_cached_fibonacci(num):
    cached_fibonacci(num)


print()
call_cached_fibonacci(10)
print(cached_fibonacci.num_calls)
"""
The cache works as a lookup table, so now fibonacci() only does the necessary 
calculations once.
"""
print()
call_cached_fibonacci(8)
print(cached_fibonacci.num_calls)
"""
NOTE: in the final call to fibonacci(8), no new calculations were needed, since 
the eighth Fibonacci number had already been calculated for fibonacci(10).

In the standard library, a Least Recently Used (LRU) cache is available as 
@functools.lru_cache. https://docs.python.org/3/library/functools.html#functools.lru_cache

This decorator has more features than the one you saw above. You should use 
@functools.lru_cache instead of writing your own cache decorator.
"""


@functools.lru_cache(maxsize=4)
def lru_fibonacci(num):
    print(f'Calculating Fibonacci({num})')
    if num < 2:
        return num
    return lru_fibonacci(num - 1) + lru_fibonacci(num - 2)


"""
The maxsize parameter specifies how many recent calls are cached. The default 
value is 128, but you can specify maxsize=None to cache all function calls. 
However, be aware that this can cause memory problems if you are caching many 
large objects.

You can use the .cache_info() method to see how the cache performs, and you can 
tune it if needed. In our example, we used an artificially small maxsize to see 
the effect of elements being removed from the cache.
"""
print()
print(lru_fibonacci(10))
print()
print(lru_fibonacci(8))
print()
print(lru_fibonacci(5))
print()
print(lru_fibonacci(8))
print()
print(lru_fibonacci(5))
