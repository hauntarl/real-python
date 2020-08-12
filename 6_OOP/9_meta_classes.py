"""DISCLAIMER:

The term metaprogramming refers to the potential for a program to have 
knowledge of or manipulate itself. Python supports a form of metaprogramming 
for classes called metaclasses.

Metaclasses are an esoteric OOP concept, lurking behind virtually all Python 
code. You are using them whether you are aware of it or not. For the most part, 
you don’t need to be aware of it. Most Python programmers rarely, if ever, have 
to think about metaclasses.

When the need arises, however, Python provides a capability that not all 
object-oriented languages support: you can get under the hood and define custom 
metaclasses. The use of custom metaclasses is somewhat controversial, as 
suggested by the following quote from Tim Peters, the Python guru who authored 
the Zen of Python:
“Metaclasses are deeper magic than 99% of users should ever worry about. If you 
wonder whether you need them, you don’t (the people who actually need them know 
with certainty that they need them, and don’t need an explanation about why).”

There are Pythonistas (as Python aficionados are known) who believe that you 
should never use custom metaclasses. That might be going a bit far, but it is 
probably true that custom metaclasses mostly aren’t necessary. If it isn’t 
pretty obvious that a problem calls for them, then it will probably be cleaner 
and more readable if solved in a simpler way.

Still, understanding Python metaclasses is worthwhile, because it leads to a 
better understanding of the internals of Python classes in general. You never 
know: you may one day find yourself in one of those situations where you just 
know that a custom metaclass is what you want.
"""


"""
- Old-Style vs. New-Style Classes:

In the Python realm, a class can be one of two varieties. No official 
terminology has been decided on, so they are informally referred to as 
old-style and new-style classes.

With old-style classes, class and type are not quite the same thing. An 
instance of an old-style class is always implemented from a single built-in 
type called instance. If obj is an instance of an old-style class, 
obj.__class__ designates the class, but type(obj) is always instance. The 
following example is taken from Python 2.7:
>>> class Foo:
...     pass
...
>>> x = Foo()
>>> x.__class__
<class __main__.Foo at 0x000000000535CC48>
>>> type(x)
<type 'instance'>

New-style classes unify the concepts of class and type. If obj is an instance 
of a new-style class, type(obj) is the same as obj.__class__:
"""


class Foo:
    pass


obj = Foo()
print(obj.__class__)
print(type(obj))
print(f'If type(obj) is obj.__class__? {type(obj) is obj.__class__}')

n = 5
d = {'x': 1, 'y': 2}
for o in (n, d, obj):
    typ = type(o)
    clss = o.__class__
    print(f'If type(o) = {typ} is o.__class__ = {clss}? {typ is clss}')


"""
- Type and Class:

In Python 3, all classes are new-style classes. Thus, in Python 3 it is 
reasonable to refer to an object’s type and its class interchangeably.

Note: In Python 2, classes are old-style by default. Prior to Python 2.2, 
new-style classes weren’t supported at all. From Python 2.2 onward, they can be 
created but must be explicitly declared as new-style.

Remember that, in Python, everything is an object. Classes are objects as well. 
As a result, a class must have a type. What is the type of a class?
"""
print()
print(type(obj), obj)
print(type(Foo), Foo)
"""
The type of x is class Foo, as you would expect. But the type of Foo, the class 
itself, is type. In general, the type of any new-style class is type.
"""
for t in int, float, dict, list, tuple:
    print(type(t), t)
"""For that matter, the type of type is type as well (yes, really)"""
print(type(type), type)


"""
type is a metaclass, of which classes are instances. Just as an ordinary object 
is an instance of a class, any new-style class in Python, and thus any class in 
Python 3, is an instance of the type metaclass.

In the above case:
- x is an instance of class Foo.
- Foo is an instance of the type metaclass.
- type is also an instance of type metaclass, so it is an instance of itself.


- Defining a Class Dynamically:

The built-in type() function, when passed one argument, returns the type of an 
object. For new-style classes, that is generally the same as the object’s 
__class__ attribute.


You can also call type() with three arguments—type(<name>, <bases>, <dct>):
- <name> specifies the class name. This becomes the __name__ attribute of the 
  class.
- <bases> specifies a tuple of the base classes from which the class inherits. 
  This becomes the __bases__ attribute of the class.
- <dct> specifies a namespace dictionary containing definitions for the class 
  body. This becomes the __dict__ attribute of the class.

Calling type() in this manner creates a new instance of the type metaclass. 
In other words, it dynamically creates a new class.

In each of the following examples, the top snippet defines a class dynamically 
with type(), while the snippet below it defines the class the usual way, with 
the class statement. In each case, the two snippets are functionally equivalent.
"""
print()


def info(obj):
    print(f"""object: {obj},
class : {obj.__class__}
bases : {obj.__class__.__bases__}
""")


FooType = type('FooType', (), {})
x = FooType()
info(x)


class FooClass:
    pass


x = FooClass()
info(x)
"""
In this first example, the <bases> and <dct> arguments passed to type() are 
both empty. No inheritance from any parent class is specified, and nothing is 
initially placed in the namespace dictionary. This is the simplest class 
definition possible.
"""
print()

BarType = type('BarType', (FooType, ), {'attr': 100})
x = BarType()
print(x.attr)
info(x)


class BarClass(FooClass):
    attr = 100


x = BarClass()
print(x.attr)
info(x)
"""
Here, <bases> is a tuple with a single element Foo, specifying the parent class 
that Bar inherits from. An attribute, attr, is initially placed into the 
namespace dictionary.
"""
print()

BazType = type(
    'BazType',
    (),
    {
        'attr': 1000,
        'attr_val': lambda x: x.attr
    }
)
x = BazType()
# NOTE: if your editor is showing an error while trying to access the attr_val()
# please ignore and run the code.
print(x.attr, x.attr_val())


class BazClass:
    attr = 1000

    def attr_val(self):
        return self.attr


x = BazClass()
print(x.attr, x.attr_val())
"""
This time, <bases> is again empty. Two objects are placed into the namespace 
dictionary via the <dct> argument. The first is an attribute named attr and the 
second a function named attr_val, which becomes a method of the defined class.
"""
print()


def f(obj):
    return f'attr = {obj.attr}'


QuxType = type(
    'QuxType',
    (),
    {
        'attr': 10000,
        'attr_val': f
    }
)
x = QuxType()
print(x.attr, x.attr_val())


class QuxClass:
    attr = 10000
    attr_val = f


x = QuxClass()
# NOTE: if your editor is showing an error while trying to access the attr_val()
# please ignore and run the code.
print(x.attr, x.attr_val())
"""
Only very simple functions can be defined with lambda in Python. In the 
following example, a slightly more complex function is defined externally then 
assigned to attr_val in the namespace dictionary via the name f.
"""
print()


"""
- Custom Metaclasses:

>>> class Foo:
...     pass
...
>>> f = Foo()

Consider this class which was defined earlier...
The expression Foo() creates a new instance of class Foo. When the interpreter 
encounters Foo(), the following occurs:
- The __call__() method of Foo’s parent class is called. Since Foo is a 
  standard new-style class, its parent class is the type metaclass, so type’s 
  __call__() method is invoked.
- That __call__() method in turn invokes the following:
    - __new__()
    - __init__()

If Foo does not define __new__() and __init__(), default methods are inherited 
from Foo’s ancestry. But if Foo does define these methods, they override those 
from the ancestry, which allows for customized behavior when instantiating Foo.
"""


def new(cls):
    x = object.__new__(cls)
    x.attr = 100
    return x


Foo.__new__ = new
f = Foo()
# NOTE: if your editor is showing an error while trying to access the attr
# please ignore and run the code.
print(f.attr)
"""
This modifies the instantiation behavior of class Foo: each time an instance of 
Foo is created, by default it is initialized with an attribute called attr, 
which has a value of 100. (Code like this would more usually appear in the 
__init__() method and not typically in __new__(). This example is contrived for 
demonstration purposes.)


Now, as has already been reiterated, classes are objects too. Suppose you 
wanted to similarly customize instantiation behavior when creating a class like 
Foo. If you were to follow the pattern above, you’d again define a custom 
method and assign it as the __new__() method for the class of which Foo is an 
instance. Foo is an instance of the type metaclass.

# Spoiler alert:  This doesn't work!
>>> def new(cls):
...     x = type.__new__(cls)
...     x.attr = 100
...     return x
...
>>> type.__new__ = new
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    type.__new__ = new
TypeError: can't set attributes of built-in/extension type 'type'

Except, as you can see, you can’t reassign the __new__() method of the type 
metaclass. Python doesn’t allow it.

This is probably just as well. type is the metaclass from which all new-style 
classes are derived. You really shouldn’t be mucking around with it anyway. But 
then what recourse is there, if you want to customize instantiation of a class?

One possible solution is a custom metaclass. Essentially, instead of mucking 
around with the type metaclass, you can define your own metaclass, which 
derives from type, and then you can muck around with that instead.

The first step is to define a metaclass that derives from type, as follows:
"""


class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 1000
        return x


"""
The definition header class Meta(type): specifies that Meta derives from type. 
Since type is a metaclass, that makes Meta a metaclass as well.

Note that a custom __new__() method has been defined for Meta. It wasn’t 
possible to do that to the type metaclass directly. The __new__() method does 
the following:
- Delegates via super() to the __new__() method of the parent metaclass (type) 
  to actually create a new class
- Assigns the custom attribute attr to the class, with a value of 100
- Returns the newly created class

Now the other half of the voodoo: Define a new class Foo and specify that its 
metaclass is the custom metaclass Meta, rather than the standard metaclass 
type. This is done using the metaclass keyword in the class definition as 
follows
"""


class Quux(metaclass=Meta):
    pass


print()
# NOTE: if your editor is showing an error while trying to access the attr
# please ignore and run the code.
print(Quux.attr)
"""
Voila! Foo has picked up the attr attribute automatically from the Meta 
metaclass. Of course, any other classes you define similarly will do likewise


In the same way that a class functions as a template for the creation of 
objects, a metaclass functions as a template for the creation of classes. 
Metaclasses are sometimes referred to as class factories.

Compare the following two examples:

- Object Factory:
>>> class Foo:
...     def __init__(self):
...         self.attr = 100
...

>>> x = Foo()
>>> x.attr
100

>>> y = Foo()
>>> y.attr
100

>>> z = Foo()
>>> z.attr
100

- Class Factory:
>>> class Meta(type):
...     def __init__(
...         cls, name, bases, dct
...     ):
...         cls.attr = 100
...
>>> class X(metaclass=Meta):
...     pass
...
>>> X.attr
100

>>> class Y(metaclass=Meta):
...     pass
...
>>> Y.attr
100

>>> class Z(metaclass=Meta):
...     pass
...
>>> Z.attr
100


Is This Really Necessary?

As simple as the above class factory example is, it is the essence of how 
metaclasses work. They allow customization of class instantiation.

Still, this is a lot of fuss just to bestow the custom attribute attr on each 
newly created class. Do you really need a metaclass just for that?

In Python, there are at least a couple other ways in which effectively the same 
thing can be accomplished:
"""
print()


# Simple Inheritance:
class Base:
    attr = 10000


class X(Base):
    pass


print(X.attr)


# Class Decorator:
def decorator(cls):
    class NewClass(cls):
        attr = 10000
    return NewClass


@decorator
class Y:
    pass


# NOTE: if your editor is showing an error while trying to access the attr
# please ignore and run the code.
print(Y.attr)
