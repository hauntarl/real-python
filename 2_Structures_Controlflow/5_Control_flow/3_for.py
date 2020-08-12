# definite iteration in python with for loop
# types of for loops:

# 1. Numeric range loop
# for i = 1 to 10
#     <loop body>
# used in languages like - BASIC, Algol, Pascal

# 2. Three expression loop
# for (i = 1; i <= 10; i++)
#     <loop body>
# used in C

# 3. Collection-Based or Iterator-Based Loop
# for i in <collection>
#     <loop body>
# Out of the above for loops, python only supports the collection-based

# Python for loop looks like this
# for <var> in <iterable>:
#     <statement(s)>

a = ['foo', 'bar', 'baz']
for i in a:
    print(i, end=' ')
print()

# In Python, iterable means an object can be used in iteration
# If an object is iterable, it can be passed to the built-in Python function
# iter(), which returns something called an iterator.
i = 'foobarbaz'
print(iter(i), i)
i = ['foo', 'bar', 'baz']
print(iter(i), i)
i = ('foo', 'bar', 'baz')
print(iter(i), i)
i = {'foo', 'bar', 'baz'}  # frozensets are also iterable
print(iter(i), i)
i = {'foo': 1, 'bar': 2, 'baz': 3}
print(iter(i), i)
# if we try other objects which are not iterable
# iter(42)  # it raises TypeError

# An iterator is essentially a value producer that yields successive values
# from its associated iterable object. The built-in function next() is used to
# obtain the next value from in iterator.
i = ['foo', 'bar', 'baz']
itr = iter(i)
print(next(itr))
print(next(itr))
print(next(itr))
# NOTE: iterator retains its state internally. It knows which values have been
# obtained already, so when you call next(), it knows what value to return next.
# When iterator runs out of values, next() raises StopIteration exception
# print(next(itr))

# You can only obtain values from an iterator in one direction. You can’t go
# backward. There is no prev() function. But you can define two independent
# iterators on the same iterable object, Each iterator maintains its own
# internal state, independent of the other

# If you want to grab all the values from an iterator at once, you can use the
# built-in list() function. Among other possible uses, list() takes an iterator
# as its argument, and returns a list consisting of all the values that the
# iterator yielded
i = ('foo', 'bar', 'baz')
print(type(i), i)
itr = iter(i)
print(type(itr), itr)
l = list(itr)
print(type(l), l)

# It isn’t necessarily advised to make a habit of this. Part of the elegance of
# iterators is that they are “lazy.” That means that when you create an
# iterator, it doesn’t generate all the items it can yield just then. It waits
# until you ask for them with next(). Items are not created until they are
# requested
# When you use list(), tuple(), or the like, you are forcing the iterator to
# generate all its values at once, so they can all be returned. If the total
# number of objects the iterator returns is very large, that may take a long
# time
# In fact, it is possible to create an iterator in Python that returns an
# endless series of objects using generator functions and itertools. If you try
# to grab all the values at once from an endless iterator, the program will hang

a = ['foo', 'bar', 'baz']
for i in a:
    print(i, end=' ')
print()
# To carry out iteration, Python does the following:
# 1. calls iter() to obtain iterator of a
# 2. calls next() repeatedly to obtain each item from the iterator in turn
# 3. Terminates the loop when next() raises the StopIteration exception
# Refer: https://realpython.com/python-for-loop/#the-guts-of-the-python-for-loop


# iterating through dictionaries
d = {'foo': 1, 'bar': 2, 'baz': 3}
itr = iter(d)

for k in d:  # this will iterate through the keys of dictionary
    print(d[k], end=' ')
print()

for v in d.values():  # will iterate through the values of dictionary
    print(v, end=' ')
print()

# In fact, you can iterate through both the keys and values of a dictionary
# simultaneously. That is because the loop variable of a for loop isn’t limited
# to just a single variable. It can also be a tuple, in which case the
# assignments are made from the items in the iterable using packing and
# unpacking, just as with an assignment statement
for i, j in [(1, 2), (3, 4), (5, 6)]:  # list of tuples
    print(i, j, end=' ')
print()

for i, j in d.items():  # items() returns a list of tuples(k, v) for given dict
    print(i, j, end=' ')
print('\n')


# the range() function: as we know Python doesn't have numeric range loop
# that's where the range() function comes into picture, as for loop accepts
# an iterable, converts it to iterator and iterates over it, range() returns
# the desired iterable object from the given input
x = range(5)
print(type(x), x)
# lets see if range is an iterable or not
itr = iter(x)
print(type(itr), itr)
# iterating over given range using for loop
for i in x:
    print(i, end=' ')
print()
# NOTE: Like iterators, range objects are lazy—the values in the specified 
# range are not generated until they are requested. Using list() or tuple() on 
# a range object forces all the values to be returned at once. This is rarely 
# necessary, and if the list is long, it can waste time and memory

# range(<begin>, <end>, <stride>) returns an iterable that yields integers 
# starting with <begin>, up to but not including <end>. If specified, <stride> 
# indicates an amount to skip between values (analogous to the stride value 
# used for string and list slicing)
for i in range(5, 20, 3):
    print(i, end=' ')
print() 
# Refer: https://realpython.com/python-for-loop/#the-range-function
# NOTE: Strictly speaking, range() isn’t exactly a built-in function. It is 
# implemented as a callable class that creates an immutable sequence type. But 
# for practical purposes, it behaves like a built-in function

# You can alter the for loop the same way you alter while loop
# using break, continue statments and else clause 
