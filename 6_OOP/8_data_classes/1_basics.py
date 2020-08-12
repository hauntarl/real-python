"""
Note: This code, as well as all other examples in this tutorial, will only work
in Python 3.7 and above.

A data class is a class typically containing mainly data, although there aren’t 
really any restrictions. It is created using the new @dataclass decorator.
"""

from math import asin, cos, radians, sin, sqrt
from typing import Any
from collections import namedtuple
from dataclasses import dataclass


@dataclass  # A data class comes with basic functionality already implemented.
# For instance, you can instantiate, print, and compare data class instances
# straight out of the box.
class DataClassCard:
    rank: str
    suit: str


queen_of_data_hearts = DataClassCard('Q', 'Hearts')
print(queen_of_data_hearts.rank, queen_of_data_hearts.suit)
print(queen_of_data_hearts == DataClassCard('Q', 'Hearts'))
print(queen_of_data_hearts is DataClassCard('Q', 'Hearts'))


# a regular class
class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
# While this is not much more code to write, you can already see signs of the
# boilerplate pain: rank and suit are both repeated three times simply to
# initialize an object. Furthermore, if you try to use this plain class, you’ll
# notice that the representation of the objects is not very descriptive, and
# for some reason a queen of hearts is not the same as a queen of hearts.


queen_of_regular_hearts = RegularCard('Q', 'Hearts')
print()
print(queen_of_regular_hearts.rank, queen_of_regular_hearts.suit)
print(queen_of_regular_hearts == RegularCard('Q', 'Hearts'))
print(queen_of_regular_hearts is RegularCard('Q', 'Hearts'))

# Seems like data classes are helping us out behind the scenes. By default,
# data classes implement a .__repr__() method to provide a nice string
# representation and an .__eq__() method that can do basic object comparisons.
# For the RegularCard class to imitate the data class above, you need to add
# these methods as well.
print()
print(repr(queen_of_data_hearts))
print(repr(queen_of_regular_hearts))


"""
- Alternatives to Data Classes:
For simple data structures, you have probably already used a tuple or a dict.
>>> queen_of_hearts_tuple = ('Q', 'Hearts')
>>> queen_of_hearts_dict = {'rank': 'Q', 'suit': 'Hearts'}


- It works. However, it puts a lot of responsibility on you as a programmer:
You need to remember that the queen_of_hearts_... variable represents a card.

For the _tuple version, you need to remember the order of the attributes. 
Writing ('Spades', 'A') will mess up your program but probably not give you an 
easily understandable error message.

If you use the _dict, you must make sure the names of the attributes are 
consistent. For instance {'value': 'A', 'suit': 'Spades'} will not work as 
expected.


- Furthermore, using these structures is not ideal:
>>> queen_of_hearts_tuple[0]  # No named access
'Q'
>>> queen_of_hearts_dict['suit']  # Would be nicer with .suit
'Hearts'

A better alternative is the namedtuple. It has long been used to create 
readable small data structures. We can in fact recreate the data class example 
above using a namedtuple.
"""
NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])

queen_of_tuple_hearts = NamedTupleCard('Q', 'Hearts')
print()
print(queen_of_tuple_hearts.rank, queen_of_tuple_hearts.suit)
print(queen_of_tuple_hearts == NamedTupleCard('Q', 'Hearts'))
print(queen_of_tuple_hearts is NamedTupleCard('Q', 'Hearts'))

# By design, a namedtuple is a regular tuple
print()
print(queen_of_tuple_hearts == ('Q', 'Hearts'))
# While this might seem like a good thing, this lack of awareness about its own
# type can lead to subtle and hard-to-find bugs, especially since it will also
# happily compare two different namedtuple classes.
Person = namedtuple('Person', ['first_name', 'last_name'])
ace_of_spades = NamedTupleCard('A', 'Spades')
print(ace_of_spades.rank, ace_of_spades.suit)
print(ace_of_spades == Person('A', 'Spades'))

"""
The namedtuple also comes with some restrictions. For instance, it is hard to 
add default values to some of the fields in a namedtuple. A namedtuple is 
also by nature immutable. That is, the value of a namedtuple can never change.
In some applications, this is an awesome feature, but in other settings, it 
would be nice to have more flexibility.

>>> card = NamedTupleCard('7', 'Diamonds')
>>> card.rank = '9'
AttributeError: can't set attribute
"""


# Basic Data Classes:
@dataclass
class Position:
    name: str
    lon: float = 0.0  # This works exactly as if you had specified the default
    lat: float = 0.0  # values in the definition of the .__init__() method
# What makes this a data class is the @dataclass decorator just above the class
# definition. Beneath the class Position: line, you simply list the fields you
# want in your data class. The : notation used for the fields is using a new
# feature in Python 3.6 called variable annotations. We will soon talk more
# about this notation and why we specify data types like str and float.
# for more: https://realpython.com/python-data-classes/#basic-data-classes

    def distance_to(self, other):
        """
        You already know that a data class is just a regular class. That means 
        that you can freely add your own methods to a data class. As an example,
        let us calculate the distance between one position and another, along 
        the Earth’s surface. One way to do this is by using the haversine 
        formula.
        """
        r = 6371  # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        h = (sin((phi_2 - phi_1) / 2)**2
             + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
        return 2 * r * asin(sqrt(h))


print()
oslo = Position('Oslo', 10.8, 59.9)
print(oslo)
print(f'{oslo.name} is at {oslo.lat}N, {oslo.lon}E')
print(Position('Null Island'))
print(Position('Greenwich', lat=51.8))
vancouver = Position('Vancouver', -123.1, 49.3)
print(vancouver)


"""
- Type Hints:

So far, we have not made a big fuss of the fact that data classes support 
typing out of the box. You have probably noticed that we defined the fields 
with a type hint: name: str says that name should be a text string (str type).

In fact, adding some kind of type hint is mandatory when defining the fields 
in your data class. Without a type hint, the field will not be a part of the 
data class. However, if you do not want to add explicit types to your data 
class, use typing.Any
"""


@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42


# While you need to add type hints in some form when using data classes, these
# types are not enforced at runtime. The following code runs without any
# problems.
print()
print(Position(3.14, 'pi day', 2018))


# Adding methods:
print()
print(oslo.distance_to(vancouver))
