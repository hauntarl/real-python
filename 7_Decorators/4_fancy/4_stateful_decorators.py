"""
- Stateful Decorators:

Sometimes, it’s useful to have a decorator that can keep track of state. As a 
simple example, we will create a decorator that counts the number of times a 
function is called.

Note: In the beginning of this guide, we talked about pure functions returning 
a value based on given arguments. Stateful decorators are quite the opposite, 
where the return value will depend on the current state, as well as the given 
arguments.
"""
import functools

from decorators import count_calls


@count_calls
def say_whee_again():
    print("Whee Again!")


say_whee_again()
say_whee_again()
print(say_whee_again.num_calls)
# The state(the number of calls to the function) is stored in the function
# attribute .num_calls on the wrapper function.


"""
- Classes as Decorators:

The typical way to maintain state is by using classes. In this section, you’ll 
see how to rewrite the @count_calls example from the previous section using a 
class as a decorator.

Recall that the decorator syntax @my_decorator is just an easier way of saying 
func = my_decorator(func). Therefore, if my_decorator is a class, it needs to 
take func as an argument in its .__init__() method. Furthermore, the class 
needs to be callable so that it can stand in for the decorated function.

For a class to be callable, you implement the special .__call__() method.
"""


class Counter:
    def __init__(self, start=0):
        self.count = start

    def __call__(self):
        """
        The .__call__() method is executed each time you try to call an 
        instance of the class
        """
        self.count += 1
        print(f'Current count is {self.count}')


print()
counter = Counter()
counter()
counter()
print(counter.count)
"""
Therefore, a typical implementation of a decorator class needs to implement 
.__init__() and .__call__()
"""


class CountCalls:
    def __init__(self, func):
        # https://docs.python.org/3/library/functools.html#functools.update_wrapper
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'Call {self.num_calls} of {self.func.__name__}')
        return self.func(*args, **kwargs)


@CountCalls
def say_whee_whee():
    print('Whee Whee!')


print()
say_whee_whee()
say_whee_whee()
print(say_whee_whee.num_calls)
"""
The .__init__() method must store a reference to the function and can do any 
other necessary initialization. The .__call__() method will be called instead 
of the decorated function. It does essentially the same thing as the wrapper() 
function in our earlier examples. Note that you need to use the 
functools.update_wrapper() function instead of @functools.wraps.

This @CountCalls decorator works the same as the one in the previous section.
"""
