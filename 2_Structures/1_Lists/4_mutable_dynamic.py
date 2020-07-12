# once created, elements can be modified
# individual values can be replaced
# order of elements can be changed
# elements can be added or removed from the list

a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
print(f'a = {a}')
print(f'reassigning a[1] = 10')
a[1] = 10
print(f'a = {a}')

# delete operation
print('\ndeleting a[1]')
del a[1]
print(f'a = {a}')

# reassigning multiple values at the same time
print('\nreassigning a[2:5] = [0, 0, 0]')
a[2:5] = [0, 0, 0]
print(f'a = {a}')
# it is not a neccessity to assign the same number of elements
# it can vary depending on what you need
print('\nreassigning a[2:] = [\'Hello\']')
a[2:] = ['Hello']
print(f'a = {a}')
print("\nreassigning a[2:3] = ['tomato', 'ham', 'lobster']")
a[2:3] = ['tomato', 'ham', 'lobster']
print(f'a = {a}')
# lists being dynamic
# NOTE: if you insert in an index instead of slice
# it will create a sublist and not expand the list itself
print("\nreassigning a[2] = ['tomato', 'ham', 'lobster']")
a[2] = ['tomato', 'ham', 'lobster']
print(f'a = {a}')

# inserting a list before a given position in list
print("\nreassigning a[1:1] = ['tomato', 'ham', 'lobster']")
a[1:1] = ['tomato', 'ham', 'lobster']
print(f'a = {a}')

# deleting multiple elements at a time
print("\ndeleting a[1:4]")
a[1:4] = []
print(f'a = {a}')

# appending elements to the list
print("\nappending ['end'] to the end of a")
a += ['end']
print(f'a = {a}')
print("\nappending ['start'] to the start of a")
a = ['start'] + a
print(f'a = {a}')
# you cannot append an object directly to the list
# that's where singleton list comes into the picture
# as the list only accepts iterable types while such operations
# NOTE: as string is an iterable, when you try to add string to list
# it will break appart each individual character of the string and add
# them separately
print("\nappending 'end' to the end of a")
a += 'end'
print(f'a = {a}')
