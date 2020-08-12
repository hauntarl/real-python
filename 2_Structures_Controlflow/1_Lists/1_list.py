# A list is a collection of arbitrary objects, muck like array

# 1. Lists are ordered
a = ['spam', 'egg', 'bacon', 'sausage']
b = ['egg', 'spam', 'sausage', 'bacon']
print(f'a = {a}')
print(f'b = {b}')
# even though the list contains the same elements,
# but their ordering is different which makes the 
# above lists different from each other
print(f'Is a == b? {a == b}')

c = ['spam', 'egg', 'bacon', 'sausage']
print(f'\nc = {c}')
print(f'Is a == c? {a == c}')
print(f'If a is c? {a is c}')


# 2. The elements of a list can be of same type but it is not a 
# requirement, python allows elements of varying types in a list
# it can contain complex objects i.e. functions, classes, modules
a = [1, 2, 3, 4]
print(f'\n\ntype(a) = {type(a)}, a = {a}')
b = [1.23, 'spam', 4, 5, 'egg', False]
print(f'type(b) = {type(b)}, b = {b}')

# list with complex objects
def foo():
    pass
import math
c = [int, len, foo, math]
# int - built-in class
# len - built-in func
# foo - user-defined func
# math - built-in module
print(f'type(c) = {type(c)}, c = {c}')


# list can be of any arbitrary length
# from 0 to as many as your computer's memory allow
# a list with a single object is sometimes called singleton list
a = []
print(f'\n\ntype(a) = {type(a)}, a = {a}')
b = ['singleton']
print(f'type(b) = {type(b)}, b = {b}')


# object in a list doesn't need to be unique 
# an object can appear multiple times in a list

