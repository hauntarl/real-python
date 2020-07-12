# Python Function Annotations
# As of version 3.0, Python provides an additional feature for documenting a
# function called a function annotation. Annotations provide a way to attach
# metadata to a function’s parameters and return value
def f(a: '<a>', b: '<b>') -> '<ret-value>':
    pass


print(f.__annotations__)
print(f.__annotations__['a'])
print(f.__annotations__['b'])
print(f.__annotations__['return'])


# NOTE: annotations aren’t restricted to string values. They can be any
# expression or object. For example, you might annotate with type objects
def g(a: int, b: str) -> float:
    pass


print()
print(g.__annotations__)
print(g.__annotations__['a'])
print(g.__annotations__['b'])
print(g.__annotations__['return'])


# An annotation can even be a composite object like a list or a dictionary, so
# it’s possible to attach multiple items of metadata to the parameters and
# return value
def area(
    r: {
        'desc': 'radius of circle',
        'type': float
    }) -> {
        'desc': 'area of circle',
        'type': float
}:
    return 3.14 * (r ** 2)


print()
print(area.__annotations__)
print(area.__annotations__['r'])
print(area.__annotations__['return'])
print(3)
# If you want to assign a default value to a parameter that has an annotation,
# then the default value goes after the annotation

# NOTE: Annotations don’t impose any semantic restrictions on the code
# whatsoever. They’re simply bits of metadata attached to the Python function
# parameters and return value. Python dutifully stashes them in a dictionary,
# assigns the dictionary to the function’s __annotations__ dunder attribute, and
# that’s it. Annotations are completely optional and don’t have any impact on
# Python function execution at all
# annotations make good documentation. You can specify the same information in
# the docstring, of course, but placing it directly in the function definition
# adds clarity. The types of the arguments and the return value are obvious on
# sight for a function header
# Refer: https://realpython.com/defining-your-own-python-function/#python-function-annotations
