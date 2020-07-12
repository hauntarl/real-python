print('INTEGERS:')
# In Python 3, there is effectively no limit to how long an integer value can be
print(123123123123123123123123123123123123123123123123 + 1)

# by default python interprets a number as base 10, literals can be prepended
# to an integer value to indicate a base other than 10
print(10)
# 0b, 0B for binary
# 0o, 0O for octal
# 0x, 0X for hexa
print(0b10)
print(0o10)
print(0x10)


# The underlying type of a Python integer, irrespective of the base
# used to specify it, is called int
print(type(0b10))
print(type(0o10))
print(type(0x10))


print('\nFLOATING-POINT NUMBERS:')

# The float type in Python designates a floating-point number.
# float values are specified with a decimal point.
# Optionally, the character e or E followed by a positive or negative integer
# may be appended to specify scientific notation
print(4.2, type(4.2))
print(.4e7, type(.4e7))
print(4.2e-4, type(4.2e-4))


# Platforms represent Python float values as 64-bit “double-precision” values
# the maximum value a float can have is approximately 1.8e308
print(1.79e308)
# Python will indicate a number greater than that by the string inf
print(1.8e308)

# The closest a nonzero number to zero is approximately 5.0e-324.
print(5.0e-324)
# Anything closer to zero than that is effectively zero
print(1.0e-325)


# Floating point numbers are represented internally as binary (base-2) fractions.
# Most decimal fractions cannot be represented exactly as binary fractions,
# in most cases the internal representation is an approximation of the actual value.
# The difference between the actual value and the represented value is very small
# and should not usually cause significant problems.
# Refer: https://docs.python.org/3.8/tutorial/floatingpoint.html

print('\nCOMPLEX NUMBERS:')

# Complex numbers are specified as <real> + <imaginary>j
# the same rules of int and float are applied to the real and imaginary part
print(2 + 3j, type(2 + 3j))
