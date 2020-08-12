# indexing in a list is zero based
# if index value is too high, python raises
# IndexError: list index out of range
# negative indexing is also available, like strings
# slicing is also available for lists

a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
print(f'a[2:5] = {a[2:5]}')
print(f'a[-4:-1] = {a[-4:-1]}')
print(f'Is a[2:5] == a[-4:-1]? {a[2:5] == a[-4:-1]}')
print(f'If a[2:5] is a[-4:-1]? {a[2:5] is a[-4:-1]}')

# omitting index is slicing is permitted
# NOTE: omitting both index will return a copy of the list
# unlike with the string, where it simply refers to the same object
b = a[:]
print(f'\nb = {b}')
print(f'Is a == b? {a == b}')
print(f'If a is b? {a is b}')
x = 'string'
y = x[:]
print(f'x = {x}')
print(f'y = {y}')
print(f'Is x == y? {x == y}')
print(f'If x is y? {x is y}')


# lists also allow you to specify strides as a third index
# also called as step, similar to strings, can be used for
# same applications as strings like: reversing...
