# Strings are sequence of character data,
# individual characters of a string can be accessed using
# numeric index (zero-based)

s = 'mybacon'
print(s[0])
print(s[len(s) - 1])
# raises IndexError if index out of range

# negative indexing: works in reverse order
print(s[-len(s)])
print(s[-1])