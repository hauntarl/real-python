# creating a class
class Dog:
    # species is a class attribute, unlike instance attributes which are
    # independent for each instance of the class, class attributes are the same
    # for every instance. Every Dog we instantiate will by default be a mammal
    # and we can change that when we create a new Dog object.
    species = 'mammal'

    # this function has a special meaning in Python class, it is called an
    # initializer (similar to a constructor), we don't actually call the func,
    # Python will automatically call the function when we instantiate the class.
    # job of initializer is to provide our object with initial attribute values
    def __init__(self, name: str, age: int) -> None:
        """
        __init__ takes 3 parameters self, name and age, when we instantiate the 
        Dog class we provide the values for name and age, this function will
        assign the object those values.

        self is very special keyword, the fact the we have to include it our
        parameters is one of those little Python quirks. We don't pass the value
        for self when we create the object, self is used to refer to the current
        object being created during instantiation.

        when we say self.age = age, we mean take the value of age we passed in
        and assign that to the new object's age attribute.
        """
        self.name = name
        self.age = age

    # instance methods: a method is basically a fucntion that belongs to a class
    # its used the exact same way as a function except we must include a self
    # parameter
    def description(self) -> str:
        """Describes the attributes of a dog"""
        return f'{self.name} is {self.age} years old {self.species}'

    def speak(self, sound: str) -> str:
        """Generates a sound made by Dog"""
        return f'{self.name} says {sound}'

    def birthday(self) -> None:
        """Increments the age attribute by one"""
        self.age += 1


help(Dog)

# NOTE: each object in Python is unique, a = Dog(), b = Dog(), a == b is false
philo = Dog('philo', 5)
mikey = Dog('mikey', 6)

print(f'\n{philo.name} is {philo.age} and {mikey.name} is {mikey.age}')
print(f'{philo.name} is a {philo.species}')
print(f'{mikey.name} is a {mikey.species}')

mikey.age = 7
philo.species = 'mouse'

print(f'\n{philo.name} is {philo.age} and {mikey.name} is {mikey.age}')
print(f'{philo.name} is a {philo.species}')
print(f'{mikey.name} is a {mikey.species}')

print()
print(mikey.description())
print(mikey.speak('Gruff gruff!'))
print('Celebrating mikey\'s birthday')
mikey.birthday()
print(mikey.description())

# NOTE: DON'T REPEAT YOURSELF (DRY) principle: if you find yourself frequently
# copying and pasting code between classes, it may be time to rethink the design
