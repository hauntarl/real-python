# at a high level super() gives you access to methods in a superclass from the
# subclass that inherits from it
# super() alone returns a temporary object of the superclass that then allows
# you to call that superclass’s methods.
# Calling the previously built methods with super() saves you from needing to
# rewrite those methods in your subclass, and allows you to swap out
# superclasses with minimal code changes

# super() in Single Inheritance
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        # using super() to call the __init__() of the Rectangle class, allowing
        # you to use it in the Square class without repeating code
        super().__init__(length, length)


rectangle = Rectangle(2, 4)
print(rectangle.area())

square = Square(4)
print(square.area())


# So what can super() do for you in single inheritance?
# Like in other object-oriented languages, it allows you to call methods of the
# superclass in your subclass. The primary use case of this is to extend the
# functionality of the inherited method
class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length


cube = Cube(3)
print()
print(cube.surface_area())
print(cube.volume())
# NOTE: super() alone won’t make the method calls for you: you have to call the
# method on the proxy object itself. super() returns a delegate object to a
# parent class, so you call the method you want directly on it
