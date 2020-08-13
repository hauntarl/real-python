"""
Decorators:
- A function that takes another function
- Extends the behavior of that function
- Without explicitly modifying the function
"""


def add_one(number):
    """A function that adds one to the number given and returns it"""
    return number + 1


print(add_one)
print(add_one(2))

add_one_also = add_one
print(add_one_also)
print(add_one_also(3))


"""Functions are first class objects"""


def hello(name):
    return f'Hello {name}'


def awesome(name):
    return f'Yo {name}, together we are the awesomest!'


print()
print(hello, hello('Chris'))
print(awesome, awesome('Gregor'))

my_list = [hello, awesome]
print(my_list[0], my_list[0]('Thomas'))
"""
If a function can be put into a list and called out of it, the same way any
other variable. Can a function be put into another function as an argument, can
one function literally call another function.
"""


def greet_bob(greeter):
    print(greeter, end=' ')
    return greeter("Bob")


print()
print(greet_bob)
print(greet_bob(hello))
print(greet_bob(awesome))


"""Inner functions"""


def parent():
    print('Printing from the parent function')

    def first_child():
        print('Printing from the first child')

    def second_child():
        print('Printing from the second child')

    print(second_child, end=' ')
    second_child()
    print(first_child, end=' ')
    first_child()


print()
parent()
parent()


"""What if you wanted to access functions that live inside another"""


def new_parent(num):
    def first_child():
        return 'Hi, I am Emma!'

    def second_child():
        return 'Call me Liam.'

    return first_child if num == 1 else second_child


print()
print(new_parent)
first = new_parent(1)
second = new_parent(2)
print(first, first())
print(second, second())
