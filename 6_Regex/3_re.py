import re

# The available regex functions in the Python re module fall into the following
# three categories:
# 1. Searching functions
# 2. Substitution functions
# 3. Utility functions

# Searching functions scan a search string for one or more matches of the
# specified regex:
# re.search(<regex>, <string>, flags=0) - Scans a string for a regex match
print(re.search(r'(\d+)', 'foo123bar'))
print(re.search(r'[a-zA-Z]+', '123FOO456'))
print(re.search(r'\d+', 'foo.bar'))
# The function returns a match object if it finds a match and None otherwise.

# re.match(<regex>, <string>, flags=0) - Looks for a regex match at the
# beginning of a string. This is identical to re.search(), except that
# re.search() returns a match if <regex> matches anywhere in <string>, whereas
# re.match() returns a match only if <regex> matches at the beginning of
# <string>
print()
print(re.match(r'\d+', '123foobar'))
print(re.match(r'\d+', 'foo123bar'))

# re.fullmatch(<regex>, <string>, flags=0) - Looks for a regex match on an
# entire string. This is similar to re.search() and re.match(), but
# re.fullmatch() returns a match only if <regex> matches <string> in its
# entirety
print()
print(re.fullmatch(r'\d+', '123foo'))
print(re.fullmatch(r'\d+', 'foo123'))
print(re.fullmatch(r'\d+', '123'))
print(re.search(r'^\d+$', '123'))
# The re.search() call, in which the \d+ regex is explicitly anchored at the
# start and end of the search string, is functionally equivalent

# re.findall(<regex>, <string>, flags=0) - Returns a list of all matches of a
# regex in a string. re.findall(<regex>, <string>) returns a list of all
# non-overlapping matches of <regex> in <string>. It scans the search string
# from left to right and returns all matches in the order found
print()
print(re.findall(r'\w+', ' foo,,,,bar:%$baz//|'))
# If <regex> contains a capturing group, then the return list contains only
# contents of the group, not the entire match
print(re.findall(r'#(\w+)#', '#foo#.#bar#.#baz#'))
# In this case, the specified regex is #(\w+)#. The matching strings are
# '#foo#', '#bar#', and '#baz#'. But the hash (#) characters don’t appear in the
# return list because they’re outside the grouping parentheses
print(re.findall(r'(\w+),(\w+)', 'foo,bar,baz,qux,quux,corge'))
# If <regex> contains more than one capturing group, then re.findall() returns a
# list of tuples containing the captured groups. The length of each tuple is
# equal to the number of groups specified

# re.finditer(<regex>, <string>, flags=0) - Returns an iterator that yields
# regex matches. Scans <string> for non-overlapping matches of <regex> and
# returns an iterator that yields the match objects from any it finds. It scans
# the search string from left to right and returns matches in the order it finds
# them
print()
for i in re.finditer(r'\w+', ' foo,,,,bar:%$baz//|'):
    print(i)
# re.findall() returns a list, whereas re.finditer() returns an iterator.
# The items in the list that re.findall() returns are the actual matching
# strings, whereas the items yielded by the iterator that re.finditer() returns
# are match objects


# Substitution Functions replace portions of a search string that match a
# specified regex
# re.sub(<regex>, <repl>, <string>, count=0, flags=0) - Returns a new string
# that results from performing replacements on a search string. Finds the
# leftmost non-overlapping occurrences of <regex> in <string>, replaces each
# match as indicated by <repl>, and returns the result. <string> remains
# unchanged
print()
s = 'foo.123.bar.789.baz'
print(re.sub(r'\d+', '#', s))
print(re.sub('[a-z]+', '(*)', s))

# Substitution by Function - If you specify <repl> as a function, then re.sub()
# calls that function for each match found. It passes each corresponding match
# object as an argument to the function to provide information about the match.
# The function return value then becomes the replacement string


def f(match_obj):
    s = match_obj.group(0)  # The matching string

    # s.isdigit() returns True if all characters in s are digits
    if s.isdigit():
        return str(int(s) * 10)
    else:
        return s.upper()


print()
print(re.sub(r'\w+', f, 'foo.10.bar.20.baz.30'))
# Limiting the Number of Replacements. If you specify a positive integer for the
# optional count parameter, then re.sub() performs at most that many
# replacements
print(re.sub(r'\w+', 'xxx', 'foo.bar.baz.qux', count=2))

# re.subn(<regex>, <repl>, <string>, count=0, flags=0) - Returns a new string
# that results from performing replacements on a search string and also returns
# the number of substitutions made
print()
print(re.subn(r'\w+', 'xxx', 'foo.bar.baz.qux'))


# Utility Functions - There are two remaining regex functions in the Python re
# module that you’ve yet to cover
# re.split(<regex>, <string>, maxsplit=0, flags=0) - Splits a string into
# substrings.
print()
print(re.split(r'\s*[,;/]\s*', 'foo,bar  ;  baz / qux corge'))
#  splits the specified string into substrings delimited by a comma (,),
# semicolon (;), or slash (/) character, surrounded by any amount of whitespace
print(re.split(r'(\s*[,;/]\s*)', 'foo,bar  ;  baz / qux'))
# If <regex> contains capturing groups, then the return list includes the
# matching delimiter strings as well
print(re.split(r'(?:\s*[,;/]\s*)', 'foo,bar  ;  baz / qux'))
# If you need to use groups but don’t want the delimiters included in the
# return list, then you can use noncapturing groups

# If the optional maxsplit argument is present and greater than zero, then
# re.split() performs at most that many splits. The final element in the return
# list is the remainder of <string> after all the splits have occurred
# Explicitly specifying maxsplit=0 is equivalent to omitting it entirely. If
# maxsplit is negative, then re.split() returns <string> unchanged

# Refer: https://realpython.com/regex-python-part-2/#re-module-functions
