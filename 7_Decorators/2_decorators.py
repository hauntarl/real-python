import functools
from datetime import datetime


def my_decorator(func):
    def wrapper():
        print('Something is happening before the function is called')
        func()
        print('Something is happening after the function is called')

    return wrapper


def say_whee():
    print('Whee!')


print(say_whee)
say_whee()

print()
say_whee = my_decorator(say_whee)
print(say_whee)
say_whee()


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()

    return wrapper


def say_whee_again():
    print('Whee again!')


print()
say_whee_again()

say_whee_again = not_during_the_night(say_whee_again)
say_whee_again()


"""Syntactic Sugar"""


def sugar_decorator(func):
    def wrapper():
        print('Something sugary happening before the function is called')
        func()
        print('Something sugary happening after the function is called')

    return wrapper


@sugar_decorator
def sugar_whee():
    print('Sugar Whee!')


print()
print(sugar_whee)
sugar_whee()


"""Reusing Decorators"""


def do_twice(func):
    # naming this inner function as wrapper is just a convention, if you are
    # using multiple decorators then it is preferred to have a specific name for
    # each wrapper to distinguish between them
    def wrapper_do_twice():
        func()
        func()

    return wrapper_do_twice


@do_twice
def reuse_whee():
    print('Reuse Whee!')


print()
reuse_whee()


"""
Passing arguments to decorators:

@do_twice
def greet(name):
    print(f'Hello {name}')

greet('World')
# raises TypeError: wrapper_do_twice() takes 0 positional arguments but was
# given 1.


- One way to counter this issue is by modifying the do_twice() to accept an
  argument
"""


def do_twice_with_one_arg(func):
    def wrapper_do_twice_with_one_arg(arg):
        func(arg)
        func(arg)

    return wrapper_do_twice_with_one_arg


@do_twice_with_one_arg
def greet(name):
    print(f'Hello {name}')


print()
greet('World')
"""
what if we try to create reuse_whee() using this decorator?

@do_twice_with_one_arg
def reuse_whee():
    print('Reuse Whee!')

reuse_whee()
# raises TypeError: wrapper_do_twice() missing one required positional argument:
# 'arg'

Is it possible to accept 1, 2, 3 or more arguments and also possible to accept
None?
"""


def reusable_do_twice(func):
    def wrapper_reusable_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper_reusable_do_twice


@reusable_do_twice
def func_greet(name):
    print(f'Hello {name}')


print()
func_greet('World!')


@reusable_do_twice
def func_whee():
    print('Whee!')


func_whee()


"""Returning values from decorated functions"""


@reusable_do_twice
def return_greet(name):
    print('Creating greeting')
    return f'Hi {name}'


print()
hi_adam = return_greet('Adam')
print(hi_adam)
# it looks like decorator ate our argument


def return_do_twice(func):
    def wrapper_return_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_return_do_twice


@return_do_twice
def fetch_greeting(name):
    print('Creating greet')
    return f'Hi {name}'


print()
hi_oliver = fetch_greeting('Oliver')
print(hi_oliver)


"""Introspection"""
print()
print(print)
print(print.__name__)
# help(print)


@return_do_twice
def fetch_whee():
    print('Whee!')


print()
fetch_whee()
print(fetch_whee)
print(fetch_whee.__name__)
"""
it is displaying the name of our wrapper function and not the one we gave,
to preserve the information about the original function, use @functools.wrap.
"""


def preserve_do_twice(func):
    @functools.wraps(func)
    def wrapper_preserve(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_preserve


@preserve_do_twice
def preserve_whee():
    print('Preserved Whee!')


print()
preserve_whee()
print(preserve_whee)
print(preserve_whee.__name__)
