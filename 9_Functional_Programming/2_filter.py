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
    Scientist(name='Ada Lovelace', field='physics', born='1867', nobel=True),
    Scientist(name='Marie Curie', field='chemistry', born='1930', nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born='1939', nobel=True),
    Scientist(name='Ada Yonath', field='astronomy', born='1928', nobel=False),
    Scientist(name='Sally Ride', field='physics', born='1951', nobel=False),
)

filter_result = filter(lambda x: x.nobel is True, scientists)
pprint(filter_result)
print()
pprint(next(filter_result))
pprint(next(filter_result))
pprint(next(filter_result))
# pprint(next(filter_result))  # StopIteration exception
"""
filter() function mainly consists of 2 parts:
1. the check function, where you apply the condition against which you want to 
   apply the filter
2. the iterable i.e. the data structure on which the filter is applied

filter() returns an iterable in Python 3 and a list if you are using Python 2,
returning an iterable makes it more efficient memory-wise
"""

print()
nobels = tuple(filter(lambda x: x.nobel is True, scientists))
pprint(nobels)
print()
pprint(tuple(filter(lambda x: x.field == 'chemistry' and x.nobel, scientists)))
print()

"""There is another way to achieve this, by using list comprehensions"""
pprint([x for x in scientists if x.nobel is True])
# NOTE: this returns a list which is mutable, maybe we don't want that
print()
pprint(tuple([x for x in scientists if x.nobel is True]))
# we are taking that intermediate list and converting it to a tuple
print()
pprint(tuple(x for x in scientists if x.nobel is True))
# instead of creating an intermediate list, we are creating a generator and
# passing it to tuple as an iterable, essentially creating an adhoc iterator
# which creates values as it iterates through
