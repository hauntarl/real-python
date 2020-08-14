"""
- Decorating Classes:

There are two different ways you can use decorators on classes. The first one 
is very close to what you have already done with functions: you can decorate 
the methods of a class. This was one of the motivations for introducing 
decorators back in the day.

Some commonly used decorators that are even built-ins in Python are 
@classmethod, @staticmethod, and @property. The @classmethod and @staticmethod 
decorators are used to define methods inside a class namespace that are not 
connected to a particular instance of that class. The @property decorator is 
used to customize getters and setters for class attributes.
"""
import functools

from decorators import debug, timer


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        """Get value of radius"""
        return self._radius

    # .radius is a mutable property: it can be set to a different value.
    # However, by defining a setter method, we can do some error testing to
    # make sure it’s not set to a nonsensical negative number. Properties are
    # accessed as attributes without parentheses
    @radius.setter
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    # .area is an immutable property: properties without .setter() methods
    # can’t be changed. Even though it is defined as a method, it can be
    # retrieved as an attribute without parentheses.
    @property
    def area(self):
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    # .cylinder_volume() is a regular method.
    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    # .unit_circle() is a class method. It’s not bound to one particular
    # instance of Circle. Class methods are often used as factory methods that
    # can create specific instances of the class.
    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    # .pi() is a static method. It’s not really dependent on the Circle class,
    # except that it is part of its namespace. Static methods can be called on
    # either an instance or the class.
    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535


c = Circle(5)
print("radius =", c.radius)
print("area =", c.area)
print("volume of cylinder with height 4 =", c.cylinder_volume(height=4))
print()

c = Circle.unit_circle()
print("radius =", c.radius)
print("area =", c.area)
print("volume of cylinder with height 4 =", c.cylinder_volume(height=4))
print()

c.radius = 2
print("radius =", c.radius)
print("area =", c.area)
print("volume of cylinder with height 4 =", c.cylinder_volume(height=4))
print()


"""Custom decorators for class methods:"""


class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_some_time(self, num_times):
        for _ in range(num_times):
            sum([i ** 2 for i in range(self.max_num)])


tw = TimeWaster(1000)
tw.waste_some_time(999)


"""
The other way to use decorators on classes is to decorate the whole class. This 
is, for example, done in the new dataclasses module in Python 3.7.

from dataclasses import dataclass

@dataclass
class PlayingCard:
    rank: str
    suit: str


The meaning of the syntax is similar to the function decorators. In the example 
above, you could have done the decoration by writing 
PlayingCard = dataclass(PlayingCard).

A common use of class decorators is to be a simpler alternative to some 
use-cases of metaclasses. In both cases, you are changing the definition of a 
class dynamically.

Writing a class decorator is very similar to writing a function decorator. The 
only difference is that the decorator will receive a class and not a function 
as an argument. In fact, all the decorators you saw above will work as class 
decorators. When you are using them on a class instead of a function, their 
effect might not be what you want. In the following example, the @timer 
decorator is applied to a class
"""


@timer
class AnotherTimeWaster:
    def __init__(self, max_num):
        self.max_num = max_num

    def waste_some_time(self, num_times):
        for _ in range(num_times):
            sum([i ** 2 for i in range(self.max_num)])


print()
tw = AnotherTimeWaster(1000)
"""
Decorating a class does not decorate its methods. Recall that @timer is just 
shorthand for TimeWaster = timer(TimeWaster).
Here, @timer only measures the time it takes to instantiate the class.

Later, you will see an example defining a proper class decorator, namely 
@singleton, which ensures that there is only one instance of a class.
"""
