print('VARIABLE ASSIGNMENT:')
# In Python, variables need not be declared or defined in advance,
# as is the case in many other programming languages.
# To create a variable, you just assign it a value and then start using it.
n = 300
print(n, type(n))
n = 1000  # new value substituted
print(n, type(n))

# Python also allows chained assignment, which makes it possible
# to assign the same value to several variables simultaneously
a = b = c = 100
print(a, b, c)


print('\nVARIABLE TYPES:')
# In many programming languages, variables are statically typed.
# That means a variable is initially declared to have a specific data type,
# and any value assigned to it during its lifetime must always have that type.
# Variables in Python are not subject to this restriction.
# In Python, a variable may be assigned a value of one type and
# then later re-assigned a value of a different type
var = 12.5
print(var, type(var))
var = 'I\'am a string now!'
print(var, type(var))


print('\nOBJECT REFRENCES:')
# Python is a highly object-oriented language.
# Virtually every item of data in a Python program is an object
# of a specific type or class.
print(300)  # creates an int obj -> assigns 300 -> displays it to console

# A Python variable is a symbolic name that is a reference or pointer to an object.
# Once an object is assigned to a variable, you can refer to the object by that name.
# But the data itself is still contained within the object
# Refer: https://realpython.com/python-variables/#object-references
n = 10  # creates new int object -> var 'n' points to that object
m = n  # creates a new reference m => points to the same object that n points to
m = 20  # creates new int object -> var 'm' points  to that object
n = 'foo'  # creates a new string object -> var 'n' points to that object.
# There is no longer any reference to the integer object 10.
# It is orphaned, and there is no way to access it.

# An object’s life begins when it is created, at which time at least one reference
# to it is created. During an object’s lifetime, additional references to it
# may be created, as you saw above, and references to it may be deleted as well.
# An object stays alive, as it were, so long as there is at least one reference to it.

# When the number of references to an object drops to zero,
# it is no longer accessible. At that point, its lifetime is over.
# Python will eventually notice that it is inaccessible and
# reclaim the allocated memory so it can be used for something else.
# In computer lingo, this process is referred to as garbage collection.


print('\nOBJECT IDENTITY:')
# Every object that is created is given a number that uniquely identifies it.
# It is guaranteed that no two objects will have the same identifier during any
# period in which their lifetimes overlap. Once an object’s reference count drops
# to zero and it is garbage collected, as happened to the 10 object above,
# then its identifying number becomes available and may be used again.
n = 10
m = n
print('id n: ', id(n), ' id m: ', id(m))
m = 20
print('id n: ', id(n), ' id m: ', id(m))
# Refer: https://realpython.com/python-variables/#object-identity
