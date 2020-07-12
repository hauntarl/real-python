# Sets are unordered.
# Set elements are unique. Duplicate elements are not allowed.
# A set itself may be modified, but the elements contained in the set
# must be of an immutable type.

# a set can be created in two ways:
# 1. using the built-in function set(<iter>)
x = set([1, 2, 3, 4, 1])
print(f'x = {x}, type(x) = {type(x)}')

x = set((1, 2, 3, 4, 1))
print(f'x = {x}, type(x) = {type(x)}')

# strings are also iterable, they can also be passed to set
s = 'iterable'
print(f's = {s}, len(s) = {len(s)}')
x = set(s)
print(f'x = {x}, len(x) = {len(x)}')


# 2. set can also be defined using curly braces, x = {obj1, obj2, ...}
x = {'foo', 'bar', 'baz', 'foo', 'qux'}
print(x)
x = {'q', 'u', 'u', 'x'}
print(x)


# a set can be empty, but python interprets empty curly braces
# as empty dict, so the only way to define empty set is using set() function
x = set()
print(type(x))
x = {}
print(type(x))


# for membership operations, in and not in operators can be used
x = {'foo', 'bar', 'baz'}
print(f"Is 'bar' in x? {'bar' in x}")
print(f"Is 'bacon' in x? {'bacon' in x}")
