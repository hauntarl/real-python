import collections

from functools import reduce
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

name_age = tuple(
    {'name': x.name, 'age': 2020 - int(x.born)}
    for x in scientists
)
pprint(name_age)

# performing a reduce operation on the ages of scientists to get the total age
totage = reduce(lambda acc, val: acc + val['age'], name_age, 0)
print(f'Total age: {totage}')
# we also could've achieved the same goal by using the built-in sum function
print(f'Total age using sum(): {sum([x["age"] for x in name_age])}\n')

"""
Why use the reduce function at all?
- reduce() function can go above and beyond in terms of what it can do.

One such operation we can do is, group scientists by their fields
"""


def reducer(acc: dict, val: Scientist):
    acc[val.field].append(val.name)
    return acc


groupby_field = reduce(
    reducer,
    scientists,
    {'math': [], 'physics': [], 'chemistry': [], 'astronomy': []},
)
pprint(groupby_field)
print()

"""
- We currently made use of an external function instead of lambda because the
  operations were a bit lengthy, but it defeats the whole purpose of clean and
  concise expression that handles it all.
- We can achieve that by using defaultdict class which comes from collections
"""
groupby_field = reduce(
    # lambda acc, val: acc[val.field].append(val.name),
    reducer,
    scientists,
    collections.defaultdict(list)
)
pprint(groupby_field)
print()

"""
defaultdict if the key doesn't exists, it will create it just in time and 
assigns a default value specified by the user, in this case it was a list.

Towards the next issue, so far we used a function which was defined in global
scope instead of lambda, lets try to do it the lambda way.

- groupby_field = reduce(
-     lambda acc, val: acc[val.field].append(val.name),
-     scientists,
-     collections.defaultdict(list)
- )
- pprint(groupby_field)

If we try to run the above code snippet, we get the following error
- TypeError: 'NoneType' object is not subscriptable

This is due to the fact that lambdas are single-expression functions in Python,
they can't have a return statement, which means the function returns whatever
is evaluated from that single-expression, in this case it will be 'None' because
the append() method does not return anything.

However, we can cheat our way around it by taking advantage of how Python 
evaluates expressions
"""
groupby_field = reduce(
    lambda acc, val: acc[val.field].append(val.name) or acc,
    scientists,
    collections.defaultdict(list)
)
pprint(groupby_field)
"""
- lambda acc, val: acc[val.field].append(val.name) or acc
as None is a Falsey value, Python will evaluate expression succeeding 'or', 
which is acc and we know that it is a Truthy value. So now our lambda function
returns the desired value.
"""
