import datetime


class Bike:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


bike = Bike('red', 25)
# 1. you are only able to see the name of the class and address of that object
# NOTE: comment the __str__() method to see the intended output
print(bike)

# 2. one way to see the contents of user-defined object is
print(bike.color, bike.mileage)


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # 3. define a to_string() method, similar to other programming langauges to
    # fetch the readable representation of object
    def to_string(self):
        return f'{{color: {self.color}, mileage: {self.mileage}}}'

    # 4. the Pythonic way to represent an object is by using the dunder methods
    # like: __str__ and __repr__
    def __str__(self):
        return f'__str__ for Car'

    # 5. Python fallbacks to this representation for the object if the __str__
    # method is not explicity defined for that class
    def __repr__(self):
        return f'__repr__ for Car'


print()
car = Car('green', 18.5)

# 3.
print(car.to_string())

# 4. whenever you try to convert an object to type string, the function
# internally calls the objects dunder __str__ method to get the string
# representation of that object
s = str(car)
print(s)
# print() also internally calls the __str__ object of each object
print(car)

# 5. using the dunder __repr__ method, this is useful when you are trying to
# inspect an object in Python console, as the console references the __repr__
# method to get the representation of that particular object
# >>> car
# >>> string representation of object in Python console
print(repr(car))


print()
# difference between __str__ and __repr__
today = datetime.date.today()
print(str(today))
print(repr(today))
#  __str__ ==> easy to read, meant for human consumption
# __repr__ ==> being unambigious, be explicit about what the object is, meant
# for internal use and something that would be easy while debugging for dev,
# NOTE: it is suggested that the result of your __repr__ should be something
# that is a valid Python and that you could just run again and re-create the
# same object, but sometimes it could become really hard to attain that in
# practice


class Truck:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # most common way of representating an object is by using only the __repr__
    # and having a specific format for the string
    def __repr__(self):
        # <class_name>(<attr1_value>, <attr2_value>, ..., <attrN_value>)
        # you could write the class name on your own or, fetch it
        return f'{self.__class__.__name__}({self.color}, {self.mileage})'


print()
truck = Truck('blue', 10)
print(truck)
print(str(truck))
print(repr(truck))


# NOTE: Containers convert their child object to string using the __repr__,
container = [bike, car, truck, today]
print()
print(container)
# even if you try to convert the container to a string, it will still use the
# __repr__ method to get string value for its child objects
print(str(container))
print(repr(container))

# bottom-line, atleast add a __repr__ method to your classes :)
