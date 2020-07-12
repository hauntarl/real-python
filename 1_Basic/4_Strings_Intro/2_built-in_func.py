# A few functions built-in to the python interpreter
# that work with string

# ord() - ordinal - returns the unicode-point for 1 char string
print(ord('a'))  # raises a TypeError if string length is != 1

# chr() - returns the unicode string of 1 char for given ordinal
print(chr(ord('a')))  # ordinal range: 0 <= i <= 0x10ffff

# len() - returns length of the container
print(len('I have some length.'))

# str() - returns string representation of an object
print(str(49.7))
print(str(1 + 2))
