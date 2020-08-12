# a datatype that contains key-value pair
# they are dynamic
# can be nested
# mutable

d = {
    'daredevil': 'kingpin',
    'x-men': 'apocalypse',
    'batman': 'bane'
}
# NOTE: as of python 3.7+ dictionaries maintain the order of insertion
print(d)
# accessing an element from dict
print(d['daredevil'])
# print(d['not-present'])  # raises KeyError as key does not exist

# adding
d['avengers'] = 'ultron'
print(d)
# updating
d['avengers'] = 'thanos'
print(d)
# delete: if key doesn't exist then it raises KeyError
del d['avengers']
print(d)

# you can Incrementally build a dictionary by initializing a variable with
# empty map
e = {}
print(e)
e['marvel'] = d
e['dc'] = {
    'batman': d['batman']
}
del d['batman']
print(e)

# Restrictions:
# Keys in a dictionary can only be used once
# Keys can only be something immutable like:
# int, float, string, bool, functions, tuple
# values can be anything

# if you try to assign a mutable object as a key
# it raises TypeError as mutable objects are not hashable
