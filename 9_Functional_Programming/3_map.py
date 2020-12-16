import collections
from pprint import pprint

Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',
])
scientists = (
    Scientist(name='Ada Lovelace', field='math', born='1815', nobel=False),
    Scientist(name='Emmy Noether', field='math', born='1882', nobel=False),
    Scientist(name='Marie Curiee', field='physics', born='1867', nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born='1930', nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born='1939', nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born='1928', nobel=False),
    Scientist(name='Sally Ride', field='physics', born='1951', nobel=False),
)

name_age = tuple(map(
    lambda x: {'name': x.name, 'age': 2020 - int(x.born)},
    scientists,
))
pprint(name_age)
print()

# we can also achieve similar result using list comprehensions
# this is considered to be more pythonic way of doing things.
name_age = tuple(
    {'name': x.name, 'age': 2020 - int(x.born)}
    for x in scientists
)
pprint(name_age)

"""
Mapping is generally used to perform transformations over the dataset.
"""
