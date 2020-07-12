# bytearray are another type of binary sequence
# no dedicated syntax for defining a bytearray literal
# always created using built-in bytearray() function
# bytearray objects are mutable, unlike bytes object

ba = bytearray('spam.egg.bacon', 'utf8')
print(ba, type(ba))
ba2 = bytearray(8)
print(ba2)
ba3 = bytearray([97, 98, 99, 100, 101])
print(ba3)
ba3[0] = 0x7a
print(ba3)

ba3[:3] = b'eg'
print(ba3)

# bytearrays can be created from bytes object
ba4 = bytearray(b'spam')  
# as they are already bytes, you don't need to put encoding tag
print(ba4) 
