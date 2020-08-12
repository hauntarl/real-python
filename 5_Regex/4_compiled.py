import re

# Compiled Regex Objects in Python - The re module supports the capability to
# precompile a regex in Python into a regular expression object that can be
# repeatedly used later
# re.compile(<regex>, flags=0) - Compiles a regex into a regular expression
# object.

# There are two ways to use a compiled regular expression object. You can
# specify it as the first argument to the re module functions in place of
# <regex>
# re_obj = re.compile(<regex>, <flags>)
# result = re.search(re_obj, <string>)
# You can also invoke a method directly from a regular expression object:
# re_obj = re.compile(<regex>, <flags>)
# result = re_obj.search(<string>)
re_obj = re.compile(r'(\d+)')
print(re.search(re_obj, 'foo123bar'))
print(re_obj.search('foo123bar'))

# In theory, you might expect precompilation to result in faster execution time
# as well. Suppose you call re.search() many thousands of times on the same
# regex. It might seem like compiling the regex once ahead of time would be more
# efficient than recompiling it each of the thousands of times it’s used.
# In practice, though, that isn’t the case. The truth is that the re module
# compiles and caches a regex when it’s used in a function call. If the same
# regex is used subsequently in the same Python code, then it isn’t recompiled.
# The compiled value is fetched from cache instead. So the performance advantage
# is minimal


# Regular Expression Object Methods
# A compiled regular expression object re_obj supports the following methods:
# re_obj.search(<string>[, <pos>[, <endpos>]])
# re_obj.match(<string>[, <pos>[, <endpos>]])
# re_obj.fullmatch(<string>[, <pos>[, <endpos>]])
# re_obj.findall(<string>[, <pos>[, <endpos>]])
# re_obj.finditer(<string>[, <pos>[, <endpos>]])
# These all behave the same way as the corresponding re functions that you’ve
# already encountered, with the exception that they also support the optional
# <pos> and <endpos> parameters. If these are present, then the search only
# applies to the portion of <string> indicated by <pos> and <endpos>, which act
# the same way as indices in slice notation
print()
s = 'foo123barbaz'
re_obj = re.compile(r'\d+')
print(re_obj.search(s))
print(re_obj.search(s, 6, 9))
# NOTE: anchors such as caret (^) and dollar sign ($) still refer to the
# start and end of the entire string, not the substring determined by <pos> and
# <endpos>

# The following methods are available for a compiled regular expression object
# re_obj as well:
# re_obj.split(<string>, maxsplit=0)
# re_obj.sub(<repl>, <string>, count=0)
# re_obj.subn(<repl>, <string>, count=0)

# Refer: https://realpython.com/regex-python-part-2/#match-object-methods-and-attributes
