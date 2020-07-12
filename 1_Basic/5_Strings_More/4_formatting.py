# string formatting methods:
# methods in this group enhance or modify the format
# of the string

# str.center(width:int, fill:str)
# if strings length is less than given width, it pads <fill>
# around the string and center's the string
# fill char must be exactly 1 char long
s = 'spam'
print(s)
print(f"'{s.center(10)}'")
print(f"'{s.center(3)}'")
print(f"'{s.center(10, '0')}'")
# print(f"'{s.center(10, '01')}'")  # raises TypeError

# str.expandtabs(tabsize=8) - replaces all the '\t' characters in target string
# to spaces
s = 'a\tb\tc'
print(f"'{s}'")
print(f"'{s.expandtabs(16)}'")

# more similar functions
# str.ljust(width, fill) - left justifies the string
# str.rjust(width, fill) - right justifies the string

# str.lstrip(str=' ') - removes any leading whitespaces(default) from the string
# and returns the copy of that string
s = '   spam bacon egg   '
print(f"'{s}'")
print(f"'{s.lstrip()}'")
link = 'http://www.realpython.com'
print(link)
print(link.lstrip('/:htp'))

# str.rstrip() - opposite of str.lstrip()
print(link.lstrip('/:pthw.').rstrip('moc.'))

# str.strip() - from both sides

# str.replace(old, new, count=-1) - replaces occurrences of old substring
# with new substring and returns the copy of the string
# by default it replaces all the substring
s = 'spam spam spam egg bacon spam spam lobster'
print(s)
print(s.replace('spam', 'tomatoes'))
print(s.replace('spam', 'tomatoes', 3))

# str.zfill(width) - left pads 0's to the target string
# if string contains any + or - sign, it is encapsulated in the length
# of the fill
s = '42'
print(s)
print(s.zfill(5))
s = '-spam'
print(s.zfill(10))
