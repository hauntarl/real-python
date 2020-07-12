# valid ways to initialize a dictionary

# 1.
d = dict([
    ('foo', 100),
    ('bar', 200),
    ('baz', 300)
])
print(d)

# 2.
d = {}
d['foo'] = 100
d['bar'] = 200
d['baz'] = 300
print(d)

# 3.
d = {'foo': 100, 'bar': 200, 'baz': 300}
print(d)

# 4.
d = dict(foo=100, bar=200, baz=300)
print(d)

# invalid
d = {
    ('foo', 100),
    ('bar', 200),
    ('baz', 300)
}
print(d, type(d))
# not a dictionary, but a set
