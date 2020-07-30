# A super() Deep Dive
# super() can also take two parameters: the first is the subclass, and the
# second parameter is an object that is an instance of that subclass
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length):
        # the super(Square, self) call is equivalent to the parameterless
        # super() call. The first parameter refers to the subclass Square,
        # while the second parameter refers to a Square object which, in this
        # case, is self
        super(Square, self).__init__(length, length)


class Cube(Square):
    def surface_area(self):
        # In this example, you are setting Square as the subclass argument to
        # super(), instead of Cube. This causes super() to start searching for
        # a matching method (in this case, .area()) at one level above Square
        # in the instance hierarchy, in this case Rectangle
        face_area = super(Square, self).area()
        # NOTE: pylint may show an error - Bad first argument 'Square' given to
        # super() - but you can ignore that as we are only testing this
        # NOTE: The parameterless call to super() is recommended and sufficient
        # for most use cases, and needing to change the search hierarchy
        # regularly could be indicative of a larger design issue.
        return face_area * 6

    def volume(self):
        # In this specific example, the behavior doesn’t change. But imagine
        # that Square also implemented an .area() function that you wanted to
        # make sure Cube did not use. Calling super() in this way allows you to
        # do that
        face_area = super(Square, self).area()
        # By including an instantiated object, super() returns a bound method:
        # a method that is bound to the object, which gives the method the
        # object’s context such as any instance attributes. If this parameter
        # is not included, the method returned is just a function, unassociated
        # with an object’s context
        # NOTE: Technically, super() doesn’t return a method. It returns a
        # proxy object. This is an object that delegates calls to the correct
        # class methods without making an additional object in order to do so.
        return face_area * self.length


cube = Cube(3)
print(cube.surface_area())
print(cube.volume())


# super() in Multiple Inheritance
# Python supports multiple inheritance, in which a subclass can inherit from
# multiple superclasses that don’t necessarily inherit from each other (also
# known as sibling classes)
class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# RightPyramid class that inherits from both Square and Triangle
class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def area(self):
        # .area() method that uses super() just like in single inheritance,
        # with the aim of it reaching the .perimeter() and .area() methods
        # defined all the way up in the Rectangle class
        # NOTE: The problem, though, is that both superclasses (Triangle and
        # Square) define a .area()
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area


pyramid = RightPyramid(2, 4)
try:
    print()
    print(pyramid.area())
except Exception as e:
    print(e)
# Python will try to call Triangle.area(). This is because of something called
# the method resolution order

# Method Resolution Order: The method resolution order (or MRO) tells Python
# how to search for inherited methods. This comes in handy when you’re using
# super() because the MRO tells you exactly where Python will look for a method
# you’re calling with super() and in what order.
# NOTE: Every class has an .__mro__ attribute that allows us to inspect the
# order
print(RightPyramid.__mro__)
# This tells us that methods will be searched first in Rightpyramid, then in
# Triangle, then in Square, then Rectangle, and then, if nothing is found, in
# object, from which all classes originate

# The problem here is that the interpreter is searching for .area() in Triangle
# before Square and Rectangle, and upon finding .area() in Triangle, Python
# calls it instead of the one you want. Because Triangle.area() expects there
# to be a .height and a .base attribute, Python throws an AttributeError


# you have some control over how the MRO is constructed. Just by changing the
# signature of the RightPyramid class, you can search in the order you want,
# and the methods will resolve correctly
class RightPyramid2(Square, Triangle):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)  # initializing Square

    def area(self):
        # .area() method that uses super() just like in single inheritance,
        # with the aim of it reaching the .perimeter() and .area() methods
        # defined all the way up in the Rectangle class
        # NOTE: The problem, though, is that both superclasses (Triangle and
        # Square) define a .area()
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area


print()
print(RightPyramid2.__mro__)
pyramid = RightPyramid2(2, 4)
print(pyramid.area())

# There are a few things wrong about these examples:
# 1. having to separate classes with same method name and signature - This
# causes issues with method resolution, because the first instance of .area()
# that is encountered in the MRO list will be called. When you’re using super()
# with multiple inheritance, it’s imperative to design your classes to
# cooperate. Part of this is ensuring that your methods are unique so that they
# get resolved in the MRO, by making sure method signatures are unique—whether
# by using method names or method parameters. Try renaming Triangle class's
# .area() method to .tri_area() to avoid complete overhaul of code


class Triangle2:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def tri_area(self):
        return 0.5 * self.base * self.height


class RightPyramid3(Square, Triangle2):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height
        super().__init__(self.base)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    # 2. The next issue here is that the code doesn’t have a delegated Triangle
    # object like it does for a Square object, so calling .area_2() will give
    # us an AttributeError since .base and .height don’t have any values
    # FIX:
    # a. All methods that are called with super() need to have a call to
    # their superclass’s version of that method. This means that you will need
    # to add super().__init__() to the .__init__() methods of Triangle and
    # Rectangle
    # b. Redesign all the .__init__() calls to take a keyword dictionary
    # Refer next tutorial to see the fix
    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area
