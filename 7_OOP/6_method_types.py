class Class:
    # can modify object instance state
    # can modify class state
    def method(self):
        return 'instance method called', self

    # can't modify object instance state
    # can modify class state
    @classmethod
    def class_method(cls):
        return 'class method called', cls

    # can't modify object instance state
    # can't modify class state
    @staticmethod
    def static_method():
        return 'static method called'


obj = Class()
print(obj.method())
print(obj.class_method())
print(obj.static_method())

print()
try:
    Class.method()  # method() missing 1 required positional argument: 'self'
except TypeError as err:
    print(err)
print(Class.class_method())
print(Class.static_method())


# Why does Python have such distinction over class methods
class Pizza:
    def __init__(self, radius, ingredients):
        self.radius = radius
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza{self.ingredients} with radius: {self.radius}'

    @classmethod
    def margherita(cls):
        return cls(10, ['cheese', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(15, ['cheese', 'tomatoes', 'ham', 'mushrooms'])

    @property
    def area(self):
        r = self.radius
        ar = self._calculate_area(r)
        return f'area of pizza with radius: {r} is {ar}'

    @staticmethod  # this serves as an utility function for the class, though
    # we could create the same function outside the class but then the intent
    # or the use of that function won't be clear, making this a staticmethod
    # for a class sends a clear message that this does not depend on the state
    # of the class/instance but its usage is related to this class.
    def _calculate_area(r):
        return r ** 2 * 3.14


print(Pizza(5, ['cheese', 'tomatoes']))
print(Pizza(10, ['cheese', 'tomatoes', 'ham']))
print(Pizza(15, ['cheese', 'tomatoes', 'mushrooms']))
# as the list of ingredients keeps increasing, the more difficult it will
# become to remember the ingredients, one way to solve this problem is by
# creating class methods to have different factory functions for the different
# types of pizza that you can create.

print()
print(Pizza.margherita())
print(Pizza.prosciutto())
# if you have class with complicated constructors that take a lot of arguments
# and you want to simplify the interface for the users then classmethods can
# really be beneficial.

# when to use static methods?
print()
print(Pizza(7, ['cheese']).area)
# NOTE: annotating helper functions like calculate_area() as static methods
# also helps us make sure that they are accidently not modifying the state of
# the class/instance as they don;t have access to any
