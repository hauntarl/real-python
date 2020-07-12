# string slicing: extract substring from a string
# syntax: s[m:n]
# s is the string
# m is the starting index <inclusive>
# n is the end position <exclusive>

print('STRING SLICING:')
s = 'mybacon'
print(s[2:5])

# omitting start index will start the slice at the
# beginning of the string
print(s[:5])

# omitting end index will extend the slice till the
# end of the string
print(s[2:])

# omitting both will return the entire string
print(s[:])
# its not a copy, but a reference to the original string
t = s[:]
print('t is s?', t is s)

print('\nEMPTY SLICE:')
# if difference between start index and end index is <= 0
# it will return an empty string
print(s[2:2])
print(s[5:2])
print('empty strings')


print('\nNEGATIVE INDEXING:')
# negative indexing for slicing
print(s[-5:-1])  # -5 inclusive, -1 exclusive


print('\nSTRIDES:')
# adding a stride: third index (: separated)
# workings as a stepping value, show many indices you
# wish to skip
print(s[::2])

# can also have a negative stride
print(s[::-2])  # starts from the last index and steps over the given index
# use case: instead of using negative start and end indices for operating
# on string in reverse direction, give a negative stride
print(s[::-1])

print('\nPALINDROME TEST:')
# check for palindrome
s = 'tacocat'
print('is input:', s, 'a palindrome?')
print(s == s[::-1])
