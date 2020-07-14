import re

#  Python code to find out whether s contains the substring '123'
s = 'foo123bar'
print('123' in s)
print(s.find('123'))
print(s.index('123'))

# rather than searching for a fixed substring like '123', suppose you wanted to
# determine whether a string contains any three consecutive decimal digit
# characters, as in the strings 'foo123bar', 'foo456bar', '234baz', and 'qux678'

# The re Module: Regex functionality in Python resides in a module named re
# re.search(<regex>, <string>) - scans <string> looking for the first location
# where the pattern <regex> matches. If a match is found, then re.search()
# returns a match object. Otherwise, it returns None
print(re.search('123', s))
if re.search('234', s):
    print('found a match')
else:
    print('no match')
# in this case, the <regex> pattern is just the plain string '123'. The pattern
# matching here is still just character-by-character comparison, pretty much the
# same as the in operator and .find()

# Python Regex Metacharacters: These have a unique meaning to the regex matching
# engine and vastly enhance the capability of the search.
# In a regex, a set of characters specified in square brackets ([]) makes up a
# character class
t = 'foo456bar'
u = '234baz'
v = 'qux678'
w = '12foo34'
print()
print(re.search('[0-9][0-9][0-9]', s))
print(re.search('[0-9][0-9][0-9]', t))
print(re.search('[0-9][0-9][0-9]', u))
print(re.search('[0-9][0-9][0-9]', v))
print(re.search('[0-9][0-9][0-9]', w))

# The dot (.) metacharacter matches any character except a newline, so it
# functions like a wildcard
print()
print(re.search('1.3', s))
print(re.search('1.3', 'foo13bar'))
# Refer: https://realpython.com/regex-python/#metacharacters-supported-by-the-re-module

# Characters contained in square brackets ([]) represent a character class—an
# enumerated set of characters to match from. A character class metacharacter
# sequence will match any single character contained in the class
print()
print(re.search('ba[artz]', 'foobarqux'))
print(re.search('ba[artz]', 'foobazqux'))
# The metacharacter sequence [artz] matches any single 'a', 'r', 't', or 'z'
# character. In the example, the regex ba[artz] matches both 'bar' and 'baz'
# (and would also match 'baa' and 'bat')

# A character class can also contain a range of characters separated by a hyphen
# (-), in which case it matches any single character within the range. For
# example, [a-z] matches any lowercase alphabetic character
print()
print(re.search('[a-z]', 'FOObar'))
# [0-9] matches any digit character
print(re.search('[0-9][0-9]', 'foo123bar'))
# [0-9a-fA-F] matches any hexadecimal digit character
print(re.search('[0-9a-fA-f]', '--- a0 ---'))
# NOTE: In the above examples, the return value is always the leftmost possible
# match. re.search() scans the search string from left to right, and as soon as
# it locates a match for <regex>, it stops scanning and returns the match.

# You can complement a character class by specifying ^ as the first character,
# in which case it matches any character that isn’t in the set. In the following
# example, [^0-9] matches any character that isn’t a digit
print()
print(re.search('[^0-9]', '12345foo'))
# NOTE: If a ^ character appears in a character class but isn’t the first
# character, then it has no special meaning and matches a literal '^' character
print(re.search('[#:^]', 'foo^bar:baz#qux'))

# if you want the character class to include a literal hyphen character. You can
# place it as the first or last character or escape it with a backslash (\)
print()
print(re.search('[-abc]', '123-456'))
print(re.search('[abc-]', '123-456'))
print(re.search(r'[ab\-c]', '123-456'))
print(re.search('[]]', 'foo[1]'))  # include ']' literal
print(re.search(r'[ab\]cd]', 'foo[1]'))  # by escaping it
# Other regex metacharacters lose their special meaning inside a character class
print(re.search('[)*+|]', '123*456'))
print(re.search('[)*+|]', '123+456'))

# \w matches any alphanumeric word character. Word characters are uppercase and
# lowercase letters, digits, and the underscore (_) character, so \w is
# essentially shorthand for [a-zA-Z0-9_]
print()
print(re.search(r'\w', '#(.a$@&'))
print(re.search('[a-zA-Z0-9_]', '#(.a$@&'))
# \W is the opposite. It matches any non-word character and is equivalent to
# [^a-zA-Z0-9_]
print(re.search(r'\W', 'a_1*3Qb'))
print(re.search('[^a-zA-Z0-9_]', 'a_1*3Qb'))

# \d matches any decimal digit character. \D is the opposite. It matches any
# character that isn’t a decimal digit
print()
print(re.search(r'\d', 'abc4def'))
print(re.search(r'\D', '234Q678'))
# \d is essentially equivalent to [0-9], and \D is equivalent to [^0-9]

# \s matches any whitespace character
print()
print(re.search(r'\s', 'foo\nbar baz'))
# \S is the opposite of \s. It matches any character that isn’t whitespace
print(re.search(r'\S', '  \n foo  \n  '))

# Escaping Metacharacters: Occasionally, you’ll want to include a metacharacter
# in your regex, except you won’t want it to carry its special meaning
# backslash (\) - Removes the special meaning of a metacharacter.
print()
s = r'foo\bar'
print(re.search(r'\\', s))


# Anchors are zero-width matches. They don’t match any actual characters in the
# search string, and they don’t consume any of the search string during parsing.
# Instead, an anchor dictates a particular location in the search string where
# a match must occur.
# ^ \A - Anchor a match to the start of <string>.
# regex ^foo stipulates that 'foo' must be present not just any old place in the
# search string, but at the beginning
print()
print(re.search('^foo', 'foobar'))
print(re.search('^foo', 'barfoo'))

# $ \Z - Anchor a match to the end of <string>.
# When the regex parser encounters $ or \Z, the parser’s current position must
# be at the end of the search string for it to find a match
print()
print(re.search('bar$', 'foobar'))
print(re.search('bar$', 'barfoo'))
# As a special case, $ (but not \Z) also matches just before a single newline at
# the end of the search string

# \b - Anchors a match to a word boundary.
# \b asserts that the regex parser’s current position must be at the beginning
# or end of a word
print()
print(re.search(r'foo\b', 'foo bar'))
print(re.search(r'foo\b', 'foo.bar'))
print(re.search(r'foo\b', 'foobar'))
# Using the \b anchor on both ends of the <regex> will cause it to match when
# it’s present in the search string as a whole word
print(re.search(r'\bbar\b', 'foo bar baz'))
print(re.search(r'\bbar\b', 'foo(bar)baz'))
print(re.search(r'\bbar\b', 'foobarbaz'))

# \B - Anchors a match to a location that isn’t a word boundary
# \B does the opposite of \b. It asserts that the regex parser’s current
# position must not be at the start or end of a word
print()
print(re.search(r'\Bfoo\B', 'foo'))
print(re.search(r'\Bfoo\B', '.foo.'))
print(re.search(r'\Bfoo\B', 'barfoobaz'))

# * - Matches zero or more repetitions of the preceding regex.
print()
print(re.search('foo-*bar', 'foobar'))
print(re.search('foo-*bar', 'foo-bar'))
print(re.search('foo-*bar', 'foo--bar'))
print(re.search('foo.*bar', '# foo $qux@grault % bar #'))

# + - Matches one or more repetitions of the preceding regex.
print()
print(re.search('foo-+bar', 'foobar'))
print(re.search('foo-+bar', 'foo-bar'))
print(re.search('foo-+bar', 'foo--bar'))

# ? - Matches zero or one repetitions of the preceding regex.
print()
print(re.search('foo-?bar', 'foobar'))
print(re.search('foo-?bar', 'foo-bar'))
print(re.search('foo-?bar', 'foo--bar'))

# *?, +?, ?? - The non-greedy (or lazy) versions of the *, +, and ? quantifiers.
# When used alone, the quantifier metacharacters *, +, and ? are all greedy,
# meaning they produce the longest possible match.
print()
print(re.search('<.*>', '%<foo> <bar> <baz>%'))
print(re.search('<.*?>', '%<foo> <bar> <baz>%'))
print(re.search('ba?', 'baaaa'))
print(re.search('ba??', 'baaaa'))
# the ? metacharacter matches zero or one occurrences of the preceding regex.
# The greedy version, ?, matches one occurrence, so ba? matches 'b' followed by
# a single 'a'. The non-greedy version, ??, matches zero occurrences, so ba??
# matches just 'b'

# {m} - Matches exactly m repetitions of the preceding regex.
print()
print(re.search('x-{3}x', 'x--x'))
print(re.search('x-{3}x', 'x---x'))

# {m,n} - Matches any number of repetitions of the preceding regex from m to n,
# inclusive
print()
for i in range(1, 6):
    s = f"x{'-' * i}x"
    print(f'{i}  {s:10}', re.search('x-{2,4}x', s))
# NOTE: Omitting m implies a lower bound of 0, and omitting n implies an
# unlimited upper bound. If you omit all of m, n, and the comma, then the curly
# braces no longer function as metacharacters. {} matches just the literal
# string '{}': allowed patterns - {m,n}, {m,}, {,n}, {,}

# {m,n}? - The non-greedy (lazy) version of {m,n}.
# {m,n} will match as many characters as possible, and {m,n}? will match as
# few as possible
print()
print(re.search('a{3,5}', 'aaaaaaaa'))
print(re.search('a{3,5}?', 'aaaaaaaa'))
