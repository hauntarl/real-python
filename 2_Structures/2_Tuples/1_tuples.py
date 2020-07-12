# identical to lists in all respect, except for
# defined differently - eclosing the elements in parenthesis ()
# immutable - data won;t be modified
# unpacking and packing
# why use tuple over lists? execution times for tuple is faster when
# manipulating them, noticable when lists are huge
# pyhton dictionaries only allows immutable types as keys so lists can't be
# used as keys

t = ('egg', 'bacon', 'spam', 'tomato', 'ham', 'lobster')
print(f'type(t) = {type(t)}, t = {t}')
# accessing tuple via indexing works the sam e as lists, inclusing slicing and
# strides, but if you try to modify the element of tuple it raises TypeError
a = 10
b = 30
print(f'a, 20, b = {a, 20, b}')  # returns a tuple
t = ()
print(f't = {t}')  # empty tuple
# singleton tuple?
t = (1)
print(f't = {t}, type(t) = {type(t)}')
# since parenthesis are also used to define operator precedence
# python evaluates the expression (2) as int 2
# to have a singleton tuple, need to include a trailing comma
t = (1,)
print(f't = {t}, type(t) = {type(t)}')
