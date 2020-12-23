"""
What is Functional Programming?
- A technique that avoids side-effects in your program by performing 
  computations mainly through the evaluations of functions and it'll rely 
  heavily on immutable data structures as well.

Why do we need to rely on immutable data structures?
- Consider a situation where you need to save a list of scientists along with 
  some basic information regarding them, like-name, field, born, noble winner.
- If we decided to create a list of dictionary to hold these elements we are 
  exposed to certain issues like:
  1. the values can be modified which can corrupt the data.
  2. we can introduces typos while entering the data into dictionary
  3. we cannot perform concurrent operations on the dictionary as the data is
     susceptible to change.

To overcome these issues, we can use something called as a namedtuple which 
comes from collections module.
"""
import collections
from pprint import pprint  # pretty print

"""this will create a new Scientist class which acts as a named tuple"""
Scientist = collections.namedtuple('Scientist', [
    'name',
    'field',
    'born',
    'nobel',
])
print(Scientist)

"""we can create objects of this class by initializing specified fields"""
ada = Scientist(name='Ada Lovelace', field='math', born='1815', nobel=False)
print(ada)

print(ada.name, ada.nobel, '\n')  # we can access the data like this
# ada.name = 'Ed Lovelace'  # AttributeError: can't set attribute

"""
now that we have created a single entity which is immutable, we also need to put
them in a tuple to achieve our goal of creating a list of scientists and their 
information.
we need to do this because even though the scientist itself is immutable but the
list data structure is not, we still can add and omit data from there.
"""
scientists = (
    Scientist(name='Ada Lovelace', field='math', born='1815', nobel=False),
    Scientist(name='Emmy Noether', field='math', born='1882', nobel=False),
    Scientist(name='Marie Curiee', field='physics', born='1867', nobel=True),
    Scientist(name='Tu Youyou', field='chemistry', born='1930', nobel=True),
    Scientist(name='Ada Yonath', field='chemistry', born='1939', nobel=True),
    Scientist(name='Vera Rubin', field='astronomy', born='1928', nobel=False),
    Scientist(name='Sally Ride', field='physics', born='1951', nobel=False),
)
pprint(scientists)

"""
In a perfect world, this is where you wanna be if you are doing any kind of
functional programming in Python. You wanna start with a solid data structure
ideally which is immutable.
"""
