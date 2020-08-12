d = {
    'daredevil': 'kingpin',
    'x-men': 'apocalypse',
    'batman': 'bane'
}

# in and not in operator
print('batman' in d)
print('deadpool' not in d)

# can be used to check existence of key before pushing a new key
# another use can o be avoid raising an error while tring to access
# a value associated with a key
print('deadpool' in d and d['deadpool'])  # short-circuit operator
print('batman' in d and d['batman'])
# using built-in method to avoid error
print(d.get('deadpool'))  # returns None if not present
print(d.get('batman'))

# items() - method, returns a list of tuples of key, value
l = d.items()
print(l, type(l))
# to iterate over these items
for i in l:
    print(i, type(i))

# keys() - method, returns a list of keys
# values() - method, returns a list  of values
k = d.keys()
print(k, type(k))
for i in k:
    print(i, type(i))

v = d.values()
print(v, type(v))
for i in v:
    print(i, type(i))

# pop() - method, removes the key and returns its value
print(d.pop('batman'))
# popitem() - method, selects the key and value pair pops out the tuple for it
print(d.popitem())

d1 = {
    'a': 'aa',
    'b': 'bb'
}
d2 = {
    'b': 'BB',
    'c': 'cc',
    'd': 'dd'
}
print(d1)
print(d2)
# update() - method, update values, or add key/value pair to the dictionary
# with tuples or keyword arguments
d2.update(c='CC', d='DD')
print(d2)
# update can be used to merge dictionaries, if key exists, value will be
# updated, if not value
d1.update(d2)
print(d1)

# clear() - method, empties the dictionaries
