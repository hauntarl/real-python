# <template>.format(<positional_argument(s)>, <keyword_argument(s)>)
# In the <template> string, replacement fields are enclosed in curly braces
# ({}). Anything not contained in curly braces is literal text that’s copied
# directly from the template to the output. If you need to include a literal
# curly bracket character, like { or }, in the template string, then you can
# escape this character by doubling it
print('{{ {0} }}'.format('foo'))

# modulo
print('%d %s cost $%.2f' % (6, 'bananas', 1.74))
# .format, with positional arguments
print('{0} {1} cost ${2}'.format(6, 'bananas', 1.74))
# raises IndexError if given index is not in range of tuple

# .format with keyword arguments instead of positional parameters to
# produce the same result
print('{quantity} {item} cost ${price}'.format(
    quantity=6,
    item='bananas',
    price=1.74
))
print('{2}.{1}.{0}/{0}{0}.{1}{1}.{2}{2}'.format('foo', 'bar', 'baz'))

# Starting with Python 3.1, you can omit the numbers in the replacement fields,
# in which case the interpreter assumes sequential order. This is referred to as
# automatic field numbering
print('{}/{}/{}'.format('foo', 'bar', 'baz'))
# raises IndexError if total braces dont match the arguments

# print('{1}{}{0}'.format('foo','bar','baz'))  # raises ValueError

# You can specify both positional and keyword arguments in one Python .format()
# call. Just note that, if you do so, then all the positional arguments must
# appear before any of the keyword arguments
print('{0}{x}{1}'.format('foo', 'bar', x='baz'))
# print('{0}{x}{1}'.format('foo', x='baz', 'bar'))  # raises SyntaxError
# Refer: https://realpython.com/python-formatted-output/#the-string-format-method-simple-replacement-fields

# The String .format() Method: Simple Replacement Fields
# syntax: {[<name>][!<conversion>][:<format_spec>]}

# <name> indicates which argument from the argument list is inserted into the
# Python format string in the given location. It’s either a number for a
# positional argument or a keyword for a keyword argument
print()
a = ['foo', 'bar', 'baz']
print('{mylist[0]}, {mylist[1]}'.format(mylist=a))  # <name> key-arg example
d = {'key1': 'foo', 'key2': 'bar'}
print('{0[key1]}, {0[key2]}'.format(d))  # <name> pos-arg example
z = 3+5j
print('{0.real}, {0.imag}'.format(z))  # accessing object's attribute

# <conversion> python can format an object as a string using three different
# built-in functions: str(), repr(), ascii() - default: str()
# <conversion> = !s, !r, !a respectively
print('{0!s}'.format('foo'))
print('{0!r}'.format('foo'))
print('{0!a}'.format('foo'))

# <format_spec> represents the guts of the Python .format() method’s
# functionality. It contains information that exerts fine control over how
# values are formatted prior to being inserted into the template string
# form :[[<fill>]<align>][<sign>][#][0][<width>][<group>][.<prec>][<type>]

# <type> : same as modulo types
print('{:d}'.format(42))
print('{:f}'.format(2.1))
print('{:s}'.format('foobar'))
print('{:x}'.format(31))
# there are some minor differences between <type> of modulo and .format()
# Refer: https://realpython.com/python-formatted-output/#the-string-format-method-simple-replacement-fields
print('{:b}'.format(257))  # modulo doesn't support binary conversion at all
print('%c' % '#')  # is valid in modulo
# print('{:c}'.format('#'))  # raises ValueError as it expects int
print('{:c}'.format(35))
print('%f%%' % 65.0)
print('{:%}'.format(0.65))

# <fill> and <align> control how formatted output is padded and positioned
# within the specified field width. These subcomponents only have meaning when
# the formatted field value doesn’t occupy the entire field width, which can
# only happen if a minimum field width is specified with <width>. If <width>
# isn’t specified, then <fill> and <align> are effectively ignored
# possible align values: <, >, ^, =
print('[{:<8s}]'.format('foo'))  # left justified
print('[{:>8s}]'.format('foo'))  # right justified
print('[{:^8s}]'.format('foo'))  # output is centered
# you can also specify a value using the equals sign (=) for the <align>
# subcomponent. This only has meaning for numeric values, and only when a sign
# is included in the output
print('{:+8d}'.format(123))
print('{:=+8d}'.format(123))
print('{:=8d}'.format(-123))
# <fill> specifies how to fill in extra space when the formatted value doesn’t
# completely fill the output width. It can be any character except for curly
# braces ({})
print('[{:->8s}]'.format('foo'))
print('[{:#<8d}]'.format(123))
print('[{:*^8s}]'.format('foo'))

# <sign> +, -
print('{:*>+6d}'.format(123))  # sign is included for both +ve and -ve
print('{:*>+6d}'.format(-123))
print('{:*>-6d}'.format(123))  # sign is included only for negative
print('{:*>-6d}'.format(-123))
print('{:*> 6d}'.format(123))  # sign for negative and space for positive
print('{:*> 6d}'.format(-123))

# <sub-component> #
print('{0:b}, {0:#b}'.format(16))
print('{0:.0f}, {0:#.0f}'.format(123))
# For any presentation type other than those shown above, the hash character
# (#) has no effect

# <sub-component> 0
print('{0:05d}'.format(123))
print('{0:>06s}'.format('foo'))
print('{0:*>05d}'.format(123))  # if <fill>, <align> specified, it is overriden

# <width> component
print('[{0:8s}]'.format('foo'))
print('[{0:8d}]'.format(123))

# <group> allows you to include a grouping separator character in numeric output
print('{0:,d}'.format(1234567))
print('{0:_d}'.format(1234567))
print('{0:,.2f}'.format(1234567.89))
print('{0:_.2f}'.format(1234567.89))

# More: https://realpython.com/python-formatted-output/#the-string-format-method-nested-replacement-fields


# f-strings
print()
s = 'foo'
# This forces conversion to be performed by repr()
print('{0!r}'.format(s))
print(f'{s!r}')
# NOTE: If you’ve mastered the Python .format() method, then you already know
# how to use Python to format f-strings!
# Refer: https://realpython.com/python-formatted-output/#the-python-formatted-string-literal-f-string
