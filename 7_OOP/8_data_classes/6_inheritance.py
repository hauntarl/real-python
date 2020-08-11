"""Inheritance: You can subclass data classes quite freely"""


from dataclasses import dataclass


@dataclass
class Position:
    name: str
    lon: float
    lat: float


@dataclass
class Capital(Position):
    country: str


print(Capital('Oslo', 10.8, 59.9, 'Norway'))
"""
Things get a little more complicated if any fields in the base class have 
default values.

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

@dataclass
class Capital(Position):
    country: str  # Does NOT work

This code will immediately crash with a TypeError complaining that “non-default 
argument ‘country’ follows default argument.” The problem is that our new 
country field has no default value, while the lon and lat fields have default 
values. The data class will try to write an .__init__() method with the 
following signature.

def __init__(name: str, lon: float = 0.0, lat: float = 0.0, country: str):
    ...


Another thing to be aware of is how fields are ordered in a subclass. Starting 
with the base class, fields are ordered in the order in which they are first 
defined. If a field is redefined in a subclass, its order does not change. For 
example, if you define Position and Capital as follows:
"""


@dataclass
class PositionWithDefaults:
    name: str
    lon: float = 0.0
    lat: float = 0.0


@dataclass
class CapitalWithDefaults(PositionWithDefaults):
    country: str = 'Unknown'
    lat: float = 40.0


print()
print(CapitalWithDefaults('Madrid', country='Spain'))
"""
Then the order of the fields in Capital will still be name, lon, lat, country. 
However, the default value of lat will be 40.0.
"""
