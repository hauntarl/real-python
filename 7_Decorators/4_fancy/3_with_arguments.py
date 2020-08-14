"""
- Decorators With Arguments:

Sometimes, it’s useful to pass arguments to your decorators. For instance,
@do_twice could be extended to a @repeat(num_times) decorator. The number of
times to execute the decorated function could then be given as an argument.

So far, the name written after the @ has referred to a function object that can
be called with another function. To be consistent, you then need
repeat(num_times=4) to return a function object that can act as a decorator.

def repeat(num_times):
    def decorator_repeat(func):
        ...  # Create and return a wrapper function
    return decorator_repeat

Typically, the decorator creates and returns an inner wrapper function, so
writing the example out in full will give you an inner function within an inner
function.
"""
import functools

from decorators import debug


@debug
def repeat(num_times):
    @debug
    def decorator_repeat(func):
        @debug
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                val = func(*args, **kwargs)
            return val
        return wrapper_repeat
    return decorator_repeat


@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")


greet('World!')
"""
It looks a little messy, but we have only put the same decorator pattern you
have seen many times by now inside one additional def that handles the
arguments to the decorator.

This wrapper_repeat() function takes arbitrary arguments and returns the value
of the decorated function, func(). This wrapper function also contains the loop
that calls the decorated function num_times times. This is no different from
the earlier wrapper functions you have seen, except that it is using the
num_times parameter that must be supplied from the outside.

Again, decorator_repeat() looks exactly like the decorator functions you have
written earlier, except that it’s named differently. That’s because we reserve
the base name—repeat()—for the outermost function, which is the one the user
will call.

As you have already seen, the outermost function returns a reference to the
decorator function.

There are a few subtle things happening in the repeat() function:
- Defining decorator_repeat() as an inner function means that repeat() will
  refer to a function object—decorator_repeat. Earlier, we used repeat without
  parentheses to refer to the function object. The added parentheses are
  necessary when defining decorators that take arguments.
- The num_times argument is seemingly not used in repeat() itself. But by
  passing num_times a closure is created where the value of num_times is stored
  until it will be used later by wrapper_repeat().
"""


"""
- Both Please, But Never Mind the Bread:

With a little bit of care, you can also define decorators that can be used both
with and without arguments. Most likely, you don’t need this, but it is nice to
have the flexibility.

As you saw in the previous section, when a decorator uses arguments, you need
to add an extra outer function. The challenge is for your code to figure out if
the decorator has been called with or without arguments.

Since the function to decorate is only passed in directly if the decorator is
called without arguments, the function must be an optional argument. This means
that the decorator arguments must all be specified by keyword. You can enforce
this with the special * syntax, which means that all following parameters are
keyword-only.

def name(_func=None, *, kw1=val1, kw2=val2, ...):  # 1
    def decorator_name(func):
        ...  # Create and return a wrapper function.

    if _func is None:
        return decorator_name                      # 2
    else:
        return decorator_name(_func)               # 3

Here, the _func argument acts as a marker, noting whether the decorator has
been called with arguments or not:
- If name has been called without arguments, the decorated function will be
  passed in as _func. If it has been called with arguments, then _func will be
  None, and some of the keyword arguments may have been changed from their
  default values. The * in the argument list means that the remaining arguments
  can’t be called as positional arguments.
- In this case, the decorator was called with arguments. Return a decorator
  function that can read and return a function.
- In this case, the decorator was called without arguments. Apply the decorator
  to the function immediately.
"""
print()


@debug
def flexible_repeat(_func=None, *, num_times=2):
    @debug
    def decorator_repeat(func):
        # try interchanging the order and see the debug messages generated.
        @debug
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                val = func(*args, **kwargs)
            return val
        return wrapper_repeat

    return decorator_repeat(_func) if _func else decorator_repeat


@flexible_repeat
def say_whee():
    print('Whee!')


print()
say_whee()
print()


@flexible_repeat(num_times=4)
def say_hello(name):
    print(f'Hello {name}')


print()
say_hello('Penny')
