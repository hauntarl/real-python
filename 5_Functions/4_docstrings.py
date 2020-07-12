# When the first statement in the body of a Python function is a string literal,
# it’s known as the function’s docstring. A docstring is used to supply
# documentation for a function. It can contain the function’s purpose, what
# arguments it takes, information about return values, or any other information
# you think would be useful.
def avg(*args):
    """Returns the average of list of numeric values."""
    return sum(args) / len(args)
# Technically, docstrings can use any of Python’s quoting mechanisms, but the
# recommended convention is to triple-quote using double-quote characters ("""),
# as shown above. If the docstring fits on one line, then the closing quotes
# should be on the same line as the opening quotes


# Multi-line docstrings are used for lengthier documentation. A multi-line
# docstring should consist of a summary line, followed by a blank line, followed
# by a more detailed description. The closing quotes should be on a line by
# themselves
def add(a=0, b=0):
    """Returns the sum of two numeric values.

    Keywords arguments:
    a -- the first operand
    b -- the second operand
    """
    return a + b
# Docstring Convention - Refer: https://www.python.org/dev/peps/pep-0257/
# When a docstring is defined, the Python interpreter assigns it to a special
# attribute of the function called __doc__. This attribute is one of a set of
# specialized identifiers in Python that are sometimes called magic attributes
# or magic methods because they provide special language functionality
# NOTE: These attributes are also referred to by the colorful nickname dunder
# attributes and dunder methods. The word dunder combines the d from double and
# under from the underscore character (_)


print(avg.__doc__)
print()
print(add.__doc__)
# you can type help(<function_name>) to display the docstring for <function_name>
help(avg)
help(add)


# It’s considered good coding practice to specify a docstring for each Python 
# function you define. For more on docstrings...
# Refer: https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings
