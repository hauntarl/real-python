# Python provides another built-in type called a frozenset, which is in all
# respects exactly like a set, except that a frozenset is immutable.
# You can perform non-modifying operations on a frozenset
# Refer: https://realpython.com/python-sets/#frozen-sets

f = frozenset(['foo', 'bar', 'baz'])
print(id(f), f)
s = {'baz', 'qux', 'quux'}

f &= s  # augmented assignment still works
print(id(f), f)
# Python does not perform augmented assignments on frozensets in place.
# The statement x &= s is effectively equivalent to x = x & s.
# It isn’t modifying the original x. It is reassigning x to a new object,
# and the object x originally referenced is gone.
# NOTE: Some objects in Python are modified in place when they are the
# target of an augmented assignment operator. But frozensets aren’t.

# USE: Frozensets are useful in situations where you want to use a set,
# but you need an immutable object. For example, you can’t define a set
# whose elements are also sets, because set elements must be immutable.
