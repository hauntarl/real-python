# Python provides two operators, is and is not,
# that determine whether the given operands have the
# same identity i.e. refer to the same object.
# This is not the same thing as equality, which means
# the two operands refer to objects that contain the
# same data but are not necessarily the same object.
x = 1001
y = 1000
print('x == y + 1 ?', x == y + 1)
print('x is y + 1 ?', x is y + 1)
