# logical expressions involve boolean operands
x = 20
print(type(x < 10))
print('callable(x)', callable(x))
# Returns whether the object is callable (i.e., some kind of function).
# Note that classes are callable, as are instances of classes with a
# __call__() method.
print('callable(len)', callable(len))

# list of operators...
# and, or, not
print('\nnot:')
print('x < 10 ?', x < 10)
print('not x < 10 ?', not x < 10)

print('\nor:')
print('x > 10 or callable(x) ?', x > 10 or callable(x))
print('x < 10 or callable(x) ?', x < 10 or callable(x))

print('\nand:')
print('x > 10 and callable(x) ?', x > 10 and callable(x))
print('x < 10 and callable(x) ?', x < 10 and callable(x))


print('\nNON-BOOLEAN VALUES:')
# All the following are considered false when evaluated in Boolean context:
# The Boolean value False
# Any value that is numerically zero (0, 0.0, 0.0+0.0j)
# An empty string
# An object of a built-in composite data type which is empty (see below)
# The special value denoted by the Python keyword 'None'
print('bool(0), bool(0.0), bool(0.0+0j)', bool(0), bool(0.0), bool(0.0+0j))
print('bool(-3), bool(3.14159), bool(1.0+1j)',
      bool(-3), bool(3.14159), bool(1.0+1j))
print('bool(''), bool(""), bool("""""")', bool(''), bool(""), bool(""""""))
print("bool('foo'), bool(\" \"), bool(''' ''')",
      bool('foo'), bool(" "), bool(''' '''))
# Python provides built-in composite data types called
# list, tuple, dict, and set. These are “container” types
# that contain other objects. An object of one of these types
# is considered false if it is empty and true if it is non-empty.
# Refer: https://realpython.com/python-operators-expressions/#logical-operators


print('\nLOGICAL EXPRESSIONS WITH NON-BOOLEAN OPERANDS:')
x = 10
print('bool(x) ?', bool(x))
print('not x ?', not x)
# in case of or/and, expression doesn't evaluate to true or false
# but instead to one of the numbers
# if a is truthy: a or b = a, a and b = b
# if a is falsy: a or b = b, a and b = a
x = 10
y = 20
print('x or y ?', x or y)
print('x and y ?', x and y)
x = 0
print('x and y ?', x and y)
# or/and are also known as short-circuit operators


print('\nSHORT-CIRCUIT OPERATORS:')
a = 10
b = 20
print('when a != 0, check if b / a > 0 ?', b / a > 0)
a = 0
# print('check if b / a > 0 ?', b / a > 0)  # raises an exception
print('when a = 0, check if b / a > 0 ?', a != 0 and b / a > 0)

print('\nSelecting a default value')
string = ''
s = string or 'default-value'
print(s)
string = 'foo'
s = string or 'default-value'
print(s)


print('\nCHAINED-COMPARISONS:')
x = 10
y = 20
z = 30
print(x < y <= z)  # y is evaluated only once
print(x < y and y <= z)  # y is evaluated twice
# if y is a function with lots of computations, then the second
# statement call the function twice compared to the first one
