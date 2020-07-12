# input() pauses program execution to allow the user to type in a line of input
# from the keyboard. Once the user presses the Enter key, all characters typed
# are read and returned as a string
s = input()
# print(s, type(s))

s = input(s + ' ')
print(s, type(s))

# input() always returns a string. If you want a numeric type, then you need to
# convert the string to the appropriate type with the int(), float(), or
# complex() built-in functions
n = input('Enter a number ')
# print(n + 100)  # raises a TypeError between str and int
print(int(n) + 100)  # if type casting fails, raises ValueError

n = int(input('Enter another number '))
print(n + 200)


# In addition to obtaining data from the user, a program will also usually need
# to present data back to the user. You can display program data to the console
# in Python with print()

# Unformatted console output
fname = 'Winston'
lname = 'Smith'
print('Name:', fname, lname)

# keyword arguments/
# Adding the keyword argument sep=<str> causes objects to be separated by the
# string <str> instead of the default single space
print('Name:', fname, lname, sep='/')
print('Name:', fname, lname, sep='...')

d = {'foo': 1, 'bar': 2, 'baz': 3}
for k, v in d.items():
    print(k, v, sep=' -> ')

# The keyword argument end=<str> causes output to be terminated by <str>
# instead of the default newline
d = {'foo': 1, 'bar': 2, 'baz': 3}
i = 0
for k, v in d.items():
    print(k, v, sep=' -> ', end=(', ' if i < len(d) - 1 else '\n'))
    i += 1
print('End of loop')

# additionaly print() accepts two additional keyword arguments, both of which
# affect handling of the output stream
# 1. file=<stream>: By default, print() sends its output to a default stream
# called sys.stdout, which is usually equivalent to the console. The
# file=<stream> argument causes output to be sent to an alternate stream
# designated by <stream> instead
# 2. flush=True: Ordinarily, print() buffers its output and only writes to the
# output stream intermittently. flush=True specifies that the output stream is
# forcibly flushed with each print()
# NOTE: These will be discussed in upcoming tutorials
