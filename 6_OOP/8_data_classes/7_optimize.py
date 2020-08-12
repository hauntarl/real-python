"""
- Optimizing Data Classes:

Slots can be used to make classes faster and use less memory. Data classes have 
no explicit syntax for working with slots, but the normal way of creating slots 
works for data classes as well. (They really are just regular classes!).
"""


from dataclasses import dataclass
from timeit import timeit


@dataclass
class SimplePosition:
    name: str
    lon: float
    lat: float


@dataclass
class SlotPosition:
    __slots__ = ['name', 'lon', 'lat']
    name: str
    lon: float
    lat: float


"""
Essentially, slots are defined using .__slots__ to list the variables on a 
class. Variables or attributes not present in .__slots__ may not be defined. 
Furthermore, a slots class may not have default values.

The benefit of adding such restrictions is that certain optimizations may be 
done. For instance, slots classes take up less memory, as can be measured using 
Pympler. (https://pythonhosted.org/Pympler/)

Similarly, slots classes are typically faster to work with. The following 
example measures the speed of attribute access on a slots data class and a 
regular data class using timeit from the standard library
"""
print(timeit(
    'slot.name',
    setup="slot=SlotPosition('Oslo', 10.8, 59.9)",
    globals=globals()
))
print(timeit(
    'simple.name',
    setup="simple=SimplePosition('Oslo', 10.8, 59.9)",
    globals=globals()
))
