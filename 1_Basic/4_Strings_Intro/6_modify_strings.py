# strings are immutable

s = 'mybacon'
print(s)
# s[2] = 'f'
# above line raises a TypeError as it doesn't allow item assignment

# to modify them:
# making a copy
t = s[:2] + 'f' + s[3:]
print(f's = {s}, t = {t},\nid of s = {id(s)}, id of t = {id(t)}')

# using the built-in string methods
s = s.replace('b', 'f')
print(s)
