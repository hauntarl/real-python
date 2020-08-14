"""
- Nesting Decorators:

You can apply several decorators to a function by stacking them on top of each 
other. Think about this as the decorators being executed in the order they are 
listed. 
"""
import functools

from decorators import debug, do_twice


@debug
@do_twice
def greet1(name):
    print(f'Hello {name}')


greet1('Eva')


@do_twice
@debug
def greet2(name):
    print(f'Hello {name}')


print()
greet2('Eva')
