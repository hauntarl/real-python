# print() supports formatting of console output that is rudimentary at best.
# You can choose how to separate printed objects, and you can specify what goes
# at the end of the printed line. That’s about it

# string modulo operator: <format_string> % <values>
# NOTE: If you’re acquainted with the printf() family of functions of C, Perl,
# or Java, then you’ll see that these don’t exist in Python. However, there is a
# quite a bit of similarity between printf() and the string modulo operator, so
# if you’re familiar with printf(), then a lot of the following will feel
# familiar
print('%d %s cost $%.3f' % (6, 'bananas', 1.74))
# In addition to representing the string modulo operation itself, the '%'
# character also denotes the conversion specifiers in the format string—in this
# case, '%d', '%s', and '%.2f'

name = 'hauntarl'
print('Hello my name is %s' % name)
# NOTE: string modulo operation isn’t only for printing. You can also format
# values and assign them to another string variable

greet = 'How are you %s?' % name
print(greet)

# Conversion specifiers appear in the <format_string> and determine how values
# are formatted when they’re inserted: %[<flags>][<width>][.<precision>]<type>
# % and <type> are required. The remaining components shown in square brackets
# are optional
# Refer: https://realpython.com/python-input-output/#the-string-modulo-operator

# Interger conversion type: d, i, u, x, X, o
# d, i, u are functionally equivalent
print('%d, %i, %u' % (42, 42, -42))
# x, X for string representation of hexadecimal integer
print('%x, %X' % (254, 255))
# o for string representation of octal number
print('%o' % 8)
# f, F for string representation of float number
print('%f, %F' % (3.14159, 3.14))
# e, E for string representation in exponential format
print('%e, %E' % (100., 1000.))

# inf and NaN
# Under some circumstances, a floating-point operation can result in a value
# that is essentially infinite. The string representation of such a number in
# Python is 'inf'.
# It also may happen that a floating-point operation produces a value that is
# not representable as a number. Python represents this with the string 'NaN'
x = float('NaN')
print('%f, %e, %F, %E' % (x, x, x, x))
x = float('Inf')
print('%f, %e, %F, %E' % (x, x, x, x))

# The g and G conversion types choose between floating point or exponential
# output, depending on the magnitude of the exponent and the value specified
# for .<precision>. (See below.) Output is the same as e/E if the exponent is
# less than -4 or not less than .<precision>. Otherwise, it’s the same as f/F
pi = 3.14
print('%g, %G' % (pi, pi))
x = .000003
print('%g, %G' % (x, x))

# Character conversion types:
# c inserts a single character. The corresponding value may be either an
# integer or a single-character string
print('%c' % 97)
print('[%c]' % 'c')
# The c conversion type supports conversion to Unicode characters as well
print('%c' % 8721)

# String conversion types:
# s, r, and a produce string output using the built-in functions str(), repr(),
# and ascii(), respectively
print('%s' % '10')
print('%r' % '10')
print('%a' % '10')

# To insert a literal '%' character into the output, specify two consecutive %
# characters in the format string. The first introduces a conversion specifier
# (as usual), and the second specifies that the conversion type is %, which
# results in a single '%' character in the output


# Width and Precision Specifiers:
# %[<flags>][<width>][.<precision>]<type>
# They determine how much horizontal space a formatted value occupies.

# <width> specifier
print('[%5s]' % 'foo')
print('[%3d]' % 4)
# If the output length is greater than <width>, then <width> has no effect

# .<precision> specifier
print('%.2f' % 123.456789)
print('%.2e' % 123.456789)
# For the g and G types, .<precision> determines the total number of significant
# digits before and after the decimal point
print('%.2g' % 123.456789)
# String values formatted with the s, r, and a types are truncated to the length
# specified by .<precision>
print('%.4s' % 'foobar')
# It is very common to see <width> and .<precision> used together
print('[%8.2f]' % 123.45678)
print('[%8.3s]' % 'foobar')
# Either of <width> or .<precision> can be specified as an asterisk character
# (*), in which case the value to be used is taken from the next item in the
# <values> tuple
print('[%*.*f]' % (10, 5, 123))

for i in range(3):
    print('[%*s]' % (i + 3, 'foo'))


# Optional conversion <flags> are specified just after the initial % character
# %[<flags>][<width>][.<precision>]<type>
# # flag: For the octal and hexadecimal conversion types, the # flag causes base
# information to be included in the formatted output
print('%#o' % 16)
print('%#x' % 16, '%#X' % 16)
# The # flag is ignored for the decimal conversion types d, i, and u.

# For floating point values, the # flag forces the output to always contain a
# decimal point
print('%.0f' % 123)
print('%#.0f' % 123)
print('%.0e' % 123)
print('%#.0e' % 123)

# The 0 Flag: When a formatted numeric value is shorter than the specified field
# width, the default behavior is to pad the field with ASCII space characters.
# The 0 flag causes padding with '0' characters instead
print('%08.2f' % 1.2)

# The - Flag: When a formatted value is shorter than the specified field width,
# it is usually right-justified in the field. The - flag causes the value to be
# left-justified in the specified field instead
print('[%-8.2f]' % 123.3)

# The + and ' ' Flags: By default, positive numeric values do not have a leading
# sign character. The + flag adds a '+' character to the left of numeric output
print('[%+5d]' % 3)
print('[%+5d]' % -3)
# The ' ' (space character) flag causes positive numeric values to be preceded 
# by a space character
print('[% d]' % 3)
print('[% d]' % -3)
