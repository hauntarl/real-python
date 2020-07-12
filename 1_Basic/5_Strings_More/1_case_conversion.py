# methods are similar to functions
# like a function, a method performs a distinct task
# unlike a function a method is tightly associated
# with a particular object
# syntax obj.foo(<args>)

s = 'egG bacOn SauSAGE loBSter'
t = 'egg123#BACON#'
u = '1 starT wiTh a digiT'

# case conversions
print('STRINGS:')
print(s)
print(t)
print(u)

print('\nCAPITALIZE:')
# capitalizes the first position of string and others are
# converted to lowercase, digits and special characters
# are ignored
print(s.capitalize())
print(t.capitalize())
print(u.capitalize())

print('\nLOWER CASE:')
# converts all alphabetic characters to lower case
print(s.lower())
print(t.lower())
print(u.lower())

print('\nSWAP CASE:')
# converts upper-case alphabetic characters to lower-case
# and vice-versa
print(s.swapcase())
print(t.swapcase())
print(u.swapcase())

print('\nTITLE CASE:')
# converts first alphabetic character of each word to an
# upper-case alphabetic character
print(s.title())
print(t.title())
print(u.title())
# gentle reminder: this function is not that smart
v = "what's happened to ted's IBM stock?"
print(v)
print(v.title())
# this method cannot understand whether 's is part of the word or not
# and also doesn't recognize acronyms like IBM

print('\nUPPER CASE:')
print(s.upper())
print(t.upper())
print(u.upper())
