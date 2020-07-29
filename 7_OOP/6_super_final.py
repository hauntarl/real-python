# Explanation at the bottom
class Rectangle:
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        super().__init__(**kwargs)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width


class Square(Rectangle):
    def __init__(self, length, **kwargs):
        super().__init__(length=length, width=length, **kwargs)


class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length


class Triangle:
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height
        super().__init__(**kwargs)

    def tri_area(self):
        return 0.5 * self.base * self.height


class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        self.slant_height = slant_height
        # passing named arguments to the super class's constructor, this with
        # minor tweak in super class's __init__ signature will allow them to be
        # initialized with arguments that make sense for that object
        super().__init__(length=base, base=base, height=slant_height)

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area


pyramid = RightPyramid(2, 4)
print(RightPyramid.__mro__)
print(pyramid.area())
print(pyramid.area_2())
# NOTE: Following the state of kwargs can be tricky here
# showing the class that owns that call, and the contents of kwargs during that
# call
# CLASS             NAMED ARGUMENTS             kwargs
# RightPyramid      base, slant_height
# Square            length                      base, height
# Rectangle         length, width               base, height
# Triangle          base, height


# What's going on? If you take a look at the Method Resolution order for this
# particular example: RightPyramid -> Square -> Rectangle -> Triangle -> object

# 1. Initially we create an instance of RightPyramid object by passing
# positional paramters for base and slant_height.

# 2. We call the __init__ method of its super class which if we refer the MRO,
# tells us that it is Square, named parameters we pass are length, base and
# height.

# 3. __init__ of Square will only accept the length argument as it matches with
# the given signature and the rest of the paramters go into the kwargs.
# NOTE: kwargs holds base and height

# 4. We call the __init__ method of Square's super class which is Rectangle,
# with named arguments of length and width along with the rest of the kwargs.

# 5. __init__ of Rectangle will accept length and width and the rest will go
# into kwargs
# NOTE: kwargs holds base and height

# 6. We call the __init__ method of Rectangle's super class which as Rectangle
# doesn't inherit from anyone can assume it to be object class, but according to
# the MRO, it is Triangle, paramters passed are the kwargs only.

# 7. __init__ of Triangle will accept base and height and the rest will go into
# kwargs
# NOTE: kwargs is empty now

# 8. We call the __init__ method of Triangle's super class which is object
# according to the MRO and pass an empty kwargs to it


# Now even if we change the MRO by changing the signature of RightPyramid class
# it would still properly initialize each and every super class that object
# depends on
# NOTE: the difference between the signatures of RightPyramid and rest of the
# classes is that RightPyramid may cause similar issues we faced in last
# tutorial if new class inherits from it, but other classes are now inheritance
# proof, meaning they are now capable of accepting the arguments which are
# required by them and passing the rest of the arguments up the MRO.
