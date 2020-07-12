# def <function_name>([<parameters>]):
#     <statement(s)>
def f():
    s = '-- Inside f()'
    print(s)


print('Before calling f()')
f()
print('After calling f()')


def stub():
    pass


stub()


# The most straightforward way to pass arguments to a Python function is with
# positional arguments (also called required arguments)
def f1(qty, item, price):
    print(f'{qty} {item} cost ${price:.2f}')


print()
f1(6, 'bananas', 1.74)
# When you’re calling a function, you can specify arguments in the form
# <keyword>=<value>. In that case, each <keyword> must match a parameter in the
# Python function definition
f1(price=1.74, qty=6, item='bananas')
# You can call a function using both positional and keyword arguments, When
# positional and keyword arguments are both present, all the positional
# arguments must come first
f1(6, price=1.74, item='bananas')


# If a parameter specified in a Python function definition has the form
# <name>=<value>, then <value> becomes a default value for that parameter.
# Parameters defined this way are referred to as default or optional parameters
def f2(qty=6, item='bananas', price=1.74):
    print(f'{qty} {item} cost ${price:.2f}')


print()
f2(4, 'apples', 2.24)
f2(4, 'apples')
f2(4)
f2()
f2(item='kumquats', qty=9)
# Default parameters allow some arguments to be omitted in function call


# Mutable Default Parameter Values
# Things can get weird if you specify a default parameter value that is a
# mutable object
def f3(my_list=[]):
    my_list.append('###')
    return my_list


print()
print(f3(['foo', 'bar', 'baz']))
print(f3([1, 2, 3, 4, 5]))
# The default value for parameter my_list is the empty list, so if f() is
# called without any arguments, then the return value is a list with the single
# element '###'
print(f3())
print(f3())
print(f3())  # unexpected result


# In Python, default parameter values are defined only once when the function
# is defined (that is, when the def statement is executed). The default value
# isn’t re-defined each time the function is called. Thus, each time you call
# f() without a parameter, you’re performing .append() on the same list
def f4(my_list=[]):
    print(id(my_list), end=' ')
    my_list.append('###')
    return my_list


print()
print(f4())
print(f4())
print(f4())


# As a workaround, consider using a default argument value that signals no
# argument has been specified. Most any value would work, but None is a common
# choice
def f5(my_list=None):
    if my_list is None:
        my_list = []
    print(id(my_list), end=' ')
    my_list.append('###')
    return my_list


print()
print(f5())
print(f5())
print(f5())


# Pass-By-Value vs Pass-By-Reference in Python
# Are parameters in Python pass-by-value or pass-by-reference? The answer is
# they’re neither, exactly. That’s because a reference doesn’t mean quite the
# same thing in Python as it does in Pascal
# Recall that in Python, every piece of data is an object. A reference points
# to an object, not a specific memory location. That means assignment isn’t
# interpreted the same way in Python as it is in Pascal
x = 5  # causes x to point to an object whose value is 5
x = 10  # the second assignment rebinds x to a different object with value 10


def z(x):
    print(f'x = {x}, id(x) = {id(x)}, In z(x)')
    x = 10
    print(f'x = {x}, id(x) = {id(x)}, Reassigning x')


print()
x = 5
print(f'x = {x}, id(x) = {id(x)}, Before calling z(x)')
z(x)
print(f'x = {x}, id(x) = {id(x)}, After calling z(x)')
# the statement x = 5 creates a reference named x bound to an object whose
# value is 5. f() is then called on line 7, with x as an argument. When f()
# first starts, a new reference called fx is created, which initially points to
# the same 5 object as x does. However, when the statement fx = 10 on line 2 is
# executed, f() rebinds fx to a new object whose value is 10. The two
# references, x and fx, are uncoupled from one another. Nothing else that f()
# does will affect x, and when f() terminates, x will still point to the object
# 5, as it did prior to the function call

# Argument passing in Python is somewhat of a hybrid between pass-by-value and
# pass-by-reference. What gets passed to the function is a reference to an
# object, but the reference is passed by value
# NOTE: Python’s argument-passing mechanism has been called pass-by-assignment
# You may also see pass-by-object, pass-by-object-reference, or pass-by-sharing


def z1(x):
    x[0] = '---'


print()
my_list = ['foo', 'bar', 'baz', 'qux']
print(my_list)
z1(my_list)
print(my_list)
# In this case, the argument to f() is a list. When f() is called, a reference
# to my_list is passed. You’ve already seen that f() can’t reassign my_list
# wholesale. If x were assigned to something else, then it would be bound to a
# different object, and the connection to my_list would be lost
# However, f() can use the reference to make modifications inside my_list. Here,
# f() has modified the first element. You can see that once the function
# returns, my_list has, in fact, been changed in the calling environment
# The same concept applies to a dictionary. NOTE: This is an example of what’s
# referred to in programming lingo as a side effect. If a side effect is a
# well-documented part of the function specification, and the user of the
# function is expressly aware of when and how the calling environment might be
# modified, then it can be okay. But a programmer may not always properly
# document side effects, or they may not even be aware that side effects are
# occurring.


# Argument passing in Python can be summarized as follows. Passing an immutable
# object, like an int, str, tuple, or frozenset, to a Python function acts like
# pass-by-value. The function can’t modify the object in the calling environment

# Passing a mutable object such as a list, dict, or set acts somewhat—but not
# exactly—like pass-by-reference. The function can’t reassign the object
# wholesale, but it can change items in place within the object, and these
# changes will be reflected in the calling environment
# Refer: https://realpython.com/defining-your-own-python-function/#argument-passing
