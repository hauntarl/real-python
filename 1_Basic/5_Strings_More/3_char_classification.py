# classify string based upon the characters that it contains

# str.isalnum() - determines whether the target string contains
# alphanumeric characters
# returns True if string is non-empty and all characters are alphanumeric
# returns False otherwise
s = 'abc123'
t = 'not alpha-numeric'
print(f"Is '{s}' alpha-numeric? {s.isalnum()}")
print(f"Is '{t}' alpha-numeric? {t.isalnum()}")

# str.isalpha() - Is target string alphabetic
u = 'ABCabc'
print(f"Is '{s}' alphabetic? {s.isalpha()}")
print(f"Is '{u}' alphabetic? {u.isalpha()}")

# str.isdigit() - determines whether the string is made up of only digits
u = '123'
print(f"Is '{s}' numeric? {s.isdigit()}")
print(f"Is '{u}' numeric? {u.isdigit()}")

# str.isidentifier() - determines whether the string is valid Python Identifier
# identifier: name used to define a varibale, function, class, etc...
# identifier must begin with an alpha or _
# can be a single character
# can be followed any alphanum or _
# cannot have other punctuation characters
s = 'def'
t = 'func'
print(f"is '{s}' a python identifier? {s.isidentifier()}")
print(f"is '{t}' a python identifier? {t.isidentifier()}")
# iskeyword(str) - to check whether the given identifier is a
# python keyword or not
# this is not a string method, but is imported from keyword module
from keyword import iskeyword
print(f"is '{s}' a python keyword? {iskeyword(s)}")
print(f"is '{t}' a python keyword? {iskeyword(t)}")

# str.isprintable() - checks whether all the alphabetic characters
# in the target string  are printable or not, rest are ignored
# unique method which returns True from empty string
s = 'a b'
t = 'a\nb'
print(f"is '{s}' printable? {s.isprintable()}")
print(f"is 'a\\nb' printable? {t.isprintable()}")

# str.isspace() - returns True if target string is non-empty
# and all the characters are whitespace chars
s = 'is space'
t = '\n\t '
print(f"does '{s}' only have whitespaces? {s.isspace()}")
print(f"does '\\n\\t ' only have whitespaces? {t.isspace()}")

# more methods:
# str.istitle() - checks for title case
# str.islower() - checks for lower case
# str.isupper() - checks for upper case
# str.isascii() - checks whether all characters are part of the ascii set
