# bytes operations support the common sequence operators
# in and not in
# concatenation(+) and replication(*) operators
# indexing and slicing
# Built-in functions: len(), min(), max()
# many methods from string objects are valid for bytes objects also
# unique methods: bytes.fromhex() and bytes.hex()

a = b'abcde'
print(f"Is b'cd' in {a}? {b'cd' in a}")

b = b'fghij'
print(a + b)

print(b * 3)

print(hex(a[0]))  # built-in function hex, return hex value for given int
print(list(a))

# each object in bytes is basically an alias for small int (0-255)
b = bytes.fromhex(' 7a 68 32 7b ')
print(b)
print(list(b))
print(b.hex())  # returns a string
