# one of the core built-in types for manipulating binary data
# a bytes object is an immutable sequence of single byte values
# each object in bytes object is a small integer (0 to 255)

# defining a bytes object is similar to defining a string literal
# requires an additional 'b' prefix
# single, double or triple quoting mechanism can be used
# only ascii characters are allowed
# any character value greater than 127 must be specified using escape sequence
# 'r' prefix can be used to disable processing of escape sequences

a = b'spam egg bacon'
print(a, type(a))

b = b'spam\xddbacon'
print(chr(b[4]))

b = rb'spam\xddbacon'
print(chr(b[4]))

# defining bytes object using built-in bytes function
# bytes(str, encoding) - creates a bytes object from that string
a = bytes('spam egg bacon', 'utf8')
print(a)

# bytes(size) - creates a bytes object consisting of null(0x00) bytes
a = bytes(8)
print(a)

# bytes(<iterable>) - can pass a list with integers from range 0-255
a = bytes([126, 127, 128, 129, 130])
print(a)
