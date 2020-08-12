# Python classes can inherit from one another, the child class inherits from
# the parent class, it will automatically implement parent's attr and methods.
# In many languages (Python included) object is the parent class of all the
# classes in the language, this includes built-in classes like int, str as well
# as any custom classes that we create

# Person represents a general person
class Person:
    description = 'general person'

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age

    def speak(self) -> None:
        print(f'My name is {self.name} and I am {self.age} years old')

    def eat(self, food: str) -> None:
        print(f'{self.name} ate {food}')

    def action(self) -> None:
        print(f'{self.name} jumps')


# Baby is a specialized version of a general person
class Baby(Person):
    description = 'baby'  # overriding the description from Person class

    # overriding the speak functionality of Person class to accurately
    # represent baby's behavior
    def speak(self) -> None:
        print('baby is speaking gibberish')

    def nap(self) -> None:
        print(f'{self.name} is taking a nap')


help(Person)
help(Baby)

person = Person('Steve', 20)
print(person.description)
person.speak()
person.eat('pasta')
person.action()

print()
# isinstance() function to check whether a particular object is instance of a
# particular class or not
print(isinstance(person, Baby))
print(isinstance(person, Person))
print(isinstance(person, object))

print()
# Baby doesn't have an initializer, yet it still asks for name and age because
# it inherits the initializer from Person class
person = Baby('Ian', 1)
print(person.description)
person.speak()
person.eat('baby food')
person.action()
person.nap()

print()
print(isinstance(person, Baby))
print(isinstance(person, Person))
print(isinstance(person, object))
