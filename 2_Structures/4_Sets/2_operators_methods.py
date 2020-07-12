x1 = {'foo', 'bar', 'baz'}
x2 = {'baz', 'qux', 'quux'}
print(x1)
print(x2)

# set union can be performed using | operator or built-in method
print(x1 | x2)
print(x1.union(x2))
print(x1)
# they both return a new object with modified values
# lets talk about the difference between the two
# | operator requires both operands to be of set type
# print(x1 | (1, 2, 3, 4))  # raises TypeError as operation is not supported
print(x1.union((1, 2, 3, 4)))
# these operations can also be performed on more than 2 operands

# other operations that can be performed are
print(x1 & x2)  # intersection
print(x1.intersection(x2))
print(x1 - x2)  # difference, elements that are present in x
print(x1.difference(x2))  # but not in y
print(x1 ^ x2)  # symmetric difference, elements present in either a or b
print(x1.symmetric_difference(x2))  # but not both
# even though ^ allows multiple operands, symmetric difference doesn't

# more methods: isdisjoint()
# determines whether or not two sets have any elements in common
# NOTE: there is no operator that corresponds to this method
x1 = {1, 2, 3}
x2 = {4, 5, 6}
print()
print(x1)
print(x2)
print(x1.isdisjoint(x2))  # when this is true then
print(x1 & x2)  # returns an empty set

# issubset(): determine whether one set is a subset of the other
x2 |= x1
print()
print(x1)
print(x2)
print(x1.issubset(x2))  # checks whether x1 is subset of x2 or not
print(x1 <= x2)
print(x1 <= x1)  # a set is considered to be a subset of itself
# a proper subset: x1 < x2: x1 is subset of x2 but not identical to x2
# NOTE: there is no built in method to check for a proper subset
print(x1 < x1)

# issuperset() / >= operator, is proper superset: > operator
# Refer: https://realpython.com/python-sets/#operating-on-a-set


# modifying a set: https://realpython.com/python-sets/#modifying-a-set
# x1.update(x2[, x3 ...]) is same as x1 |= x2 [| x3 ...]
# x1.intersection_update(x2[, x3 ...]) is same as x1 &= x2 [& x3 ...]
# x1.difference_update(x2) and x1 -= x2 update x1
# x1.symmetric_difference_update(x2) and x1 ^= x2 update x1

# other methods: x.add(obj) where obj must be a single immutable object
# x.remove(ele) raises KeyError if element is not in the set
# x.discard(ele) also removes element, but does not raise error if ele not present
# x.pop() removes any arbitrarily chosen element, raises KeyError if x is empty
# x.clear() remove all
