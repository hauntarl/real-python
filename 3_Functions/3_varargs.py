# Argument tuple packing
# When a parameter name in a Python function definition is preceded by an
# asterisk (*), it indicates argument tuple packing. Any corresponding arguments
# in the function call are packed into a tuple that the function can refer to by
# the given parameter name
def f(*atp):  # widely used variable name is *args
    print(atp, type(atp), len(atp))
    for a in atp:
        print(a, end=', ')
    print()


f(1, 2, 3, 4, 5)


def avg(*atp):
    sum = 0
    for a in atp:
        sum += a
    return sum / len(atp)


average = avg(1, 2, 3, 4, 5)
print()
print(average)


def tidy_avg(*atp):
    return sum(atp) / len(atp)


average = tidy_avg(1, 2, 3, 4, 5)
print(average)


# Argument tuple unpacking
# An analogous operation is available on the other side of the equation in a
# Python function call. When an argument in a function call is preceded by an
# asterisk (*), it indicates that the argument is a tuple that should be
# unpacked and passed to the function as separate values
def z(x, y, z):
    print(x, y, z)


t = (1, 2, 3)
print()
z(*t)
# Although this type of unpacking is called tuple unpacking, it doesn’t only
# work with tuples. The asterisk (*) operator can be applied to any iterable in
# a Python function call. You can even use tuple packing and unpacking at the
# same time


# Argument dictionary packing
# Python has a similar operator, the double asterisk (**), which can be used
# with Python function parameters and arguments to specify dictionary packing
# and unpacking. Preceding a parameter in a Python function definition by a
# double asterisk (**) indicates that the corresponding arguments, which are
# expected to be key=value pairs, should be packed into a dictionary
def d(**adp):  # widely used variable name is *kwargs (keyword args)
    print(adp, type(adp), len(adp))
    for k, v in adp.items():
        print(k, v, end=", ")
    print()


print()
d(foo=1, bar=2, baz=3)
# Argument dictionary unpacking is analogous to argument tuple unpacking. When
# the double asterisk (**) precedes an argument in a Python function call, it
# specifies that the argument is a dictionary that should be unpacked, with the
# resulting items passed to the function as keyword arguments
d(**dict(foo=1, bar=2, baz=3))
# Refer: https://realpython.com/python-kwargs-and-args


# All three—standard positional parameters, *args, and **kwargs—can be used in
# one Python function definition. If so, then they should be specified in that
# order.
def farg(a, b, *args, **kwargs):
    print(F'a = {a}')
    print(F'b = {b}')
    print(F'args = {args}')
    print(F'kwargs = {kwargs}')


print()
farg(1, 2, 'foo', 'bar', 'baz', 'qux', x=100, y=200, z=300)


# Multiple Unpackings in a Python Function Call
# Python version 3.5 introduced support for additional unpacking generalizations
a = [1, 2, 3]
b = (4, 5, 6)
c = {7, 8, 9}
print()
f(*a, *b, *c)
# You can also specify multiple dictionary unpackings in a Python function call


# Refer: https://realpython.com/defining-your-own-python-function/#keyword-only-arguments
# Refer: https://realpython.com/defining-your-own-python-function/#positional-only-arguments

# NOTE: This is Python 3.8
def func(x, y, /, z, w, *, a, b):
    print(x, y, z, w, a, b)


print()
func(1, 2, z=3, w=4, a=5, b=6)
func(1, 2, 3, w=4, a=5, b=6)
# x and y are positional-only
# a and b are keyword-only
# z and w may be specified positionally or by keyword
