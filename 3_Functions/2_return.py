# A return statement in a Python function serves two purposes:
# It immediately terminates the function and passes execution control back to the caller.
# It provides a mechanism by which the function can pass data back to the caller.
def f():
    print('foo')
    print('bar')
    return


f()
# In this example, the return statement is actually superfluous. A function will
#  return to the caller when it falls off the end—that is, after the last
# statement of the function body is executed. So, this function would behave
# identically without the return statement


def f1(x):
    if x < 0:
        return
    if x > 100:
        return
    print(x)


print()
f1(101)
f1(-1)
f1(50)
# The first two calls to f() don’t cause any output, because a return statement
# is executed and the function exits prematurely, before the print() statement
# This sort of paradigm can be useful for error checking in a function
# def f():
#     if error_cond1:
#         return
#     if error_cond2:
#         return
#     if error_cond3:
#         return
#     <normal processing>


def f2():
    return 'foo'


print(f2())
# A function can return any type of object


# If multiple comma-separated expressions are specified in a return statement,
# then they’re packed and returned as a tuple:
def f3():
    return 'foo', 'bar', 'baz', 'qux'


print(type(f3()))


# When no return value is given, a Python function returns the special Python
# value None. The same thing happens if the function body doesn’t contain a
# return statement at all and the function falls off the end
def f4():
    return


print(f4())


# Revisiting the side-effects
def double1(x):
    x *= 2
    print(f'In double1(x), x = {x}')


print()
x = 10
print(f'Before calling double1(x), x = {x}')
double1(x)
print(f'After calling double1(x), x = {x}')


# To update the value of x at caller end
def double2(x):
    x *= 2
    print(f'In double2(x), x = {x}')
    return x


print()
print(f'Before calling double2(x), x = {x}')
x = double2(x)
print(f'After calling double2(x), x = {x}')


# using the side effect
def double_list_while(x):
    i = 0
    while i < len(x):
        x[i] *= 2
        i += 1


# without using the side effect
def double_list_for(x):
    r = []
    for i in x:
        r.append(i * 2)
    return r


a = [1, 2, 3, 4, 5]
print()
print(a)
print(double_list_while(a), a)
print(double_list_for(a), a)
