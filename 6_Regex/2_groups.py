import re
# Grouping Constructs and Backreferences: breaks up a regex in Python into
# subexpressions or groups -
# 1. Grouping: A group represents a single syntactic entity. Additional
# metacharacters apply to the entire group as a unit
# 2. Capturing: Some grouping constructs also capture the portion of the search
# string that matches the subexpression in the group. You can retrieve captured
# matches later through several different mechanisms
# (<regex>) - Defines a subexpression or group.
print(re.search('(bar)', 'foo bar baz'))
print(re.search('bar', 'foo bar baz'))

# Treating a Group as a Unit. A quantifier metacharacter that follows a group
# operates on the entire subexpression specified in the group as a single unit
print(re.search('(bar)+', 'foo bar baz'))
print(re.search('(bar)+', 'foo barbar baz'))
print(re.search('(bar)+', 'foo barbarbarbar baz'))
print(re.search('(ba[rz]){2,4}(qux)?', 'bazbarbazqux'))
print(re.search('(ba[rz]){2,4}(qux)?', 'barbar'))
# regex (ba[rz]){2,4}(qux)? matches 2 to 4 occurrences of either 'bar' or 'baz',
# optionally followed by 'qux'

# nest grouping parentheses
print()
print(re.search(r'(foo(bar)?)+(\d\d\d)?', 'foofoobar'))
print(re.search(r'(foo(bar)?)+(\d\d\d)?', 'foofoobar123'))
print(re.search(r'(foo(bar)?)+(\d\d\d)?', 'foofoo123'))
# at least one occurrence of 'foo' optionally followed by 'bar', all optionally
# followed by three decimal digit characters


# m.groups() - Returns a tuple containing all the captured groups from a regex
# match
m = re.search(r'(\w+),(\w+),(\w+)', 'foo,quux,baz')
print()
print(m)
print(m.groups())
# Each of the three (\w+) expressions matches a sequence of word characters.
# The full regex (\w+),(\w+),(\w+) breaks the search string into three
# comma-separated tokens
# NOTE: Notice that the tuple contains the tokens but not the commas that
# appeared in the search string. That’s because the word characters that make
# up the tokens are inside the grouping parentheses but the commas aren’t.

# m.group(<n>) - Returns a string containing the <n>th captured match
print(m.group(1))
print(m.group(2))
print(m.group(3))
# Since the numbering of captured matches is one-based, and there isn’t any
# group numbered zero, m.group(0) has a special meaning
print(m.group(0))  # returns the entire match (m.group() does the same)
# With multiple arguments, .group() returns a tuple containing the specified
# captured matches in the given order
print(m.group(2, 3))

# (?P<name><regex>) - Creates a named captured group.
# This metacharacter sequence is similar to grouping parentheses in that it
# creates a group matching <regex> that is accessible through the match object
# or a subsequent backreference. The difference in this case is that you
# reference the matched group by its given symbolic <name> instead of by its
# number.
m = re.search(r'(?P<w1>\w+),(?P<w2>\w+),(?P<w3>\w+)', 'foo,quux,baz')
print()
print(m)
print(m.groups())
print(m.group('w1'))
print(m.group('w2'))
# NOTE: You can still access groups with symbolic names by number if you wish


# (?:<regex>) - Creates a non-capturing group.
# (?:<regex>) is just like (<regex>) in that it matches the specified <regex>.
# But (?:<regex>) doesn’t capture the match for later retrieval
m = re.search(r'(\w+),(?:\w+),(\w+)', 'foo,quux,baz')
print()
print(m)
print(m.groups())
# the middle word 'quux' sits inside non-capturing parentheses, so it’s missing
# from the tuple of captured groups. It isn’t retrievable from the match object
# Why? You may have a situation where you need this grouping feature, but you
# don’t need to do anything with the value later, so you don’t really need to
# capture it. If you use non-capturing grouping, then the tuple of captured
# groups won’t be cluttered with values you don’t actually need to keep
# Additionally, it takes some time and memory to capture a group. If the code
# that performs the match executes many times and you don’t capture groups that
# you aren’t going to use later, then you may see a slight performance advantage


# Vertical bar, or pipe (|) - Specifies a set of alternatives on which to match
print()
print(re.search('foo|bar|baz', 'bar'))
print(re.search('foo|bar|baz', 'quux'))
# NOTE: Alternation is non-greedy. The regex parser looks at the expressions
# separated by | in left-to-right order and returns the first match that it
# finds. The remaining expressions aren’t tested, even if one of them would
# produce a longer match
print(re.search('foo|grault', 'foograult'))
re.search('(foo|bar|baz)+', 'foofoofoo')
re.search('(foo|bar|baz)+', 'bazbazfoo')

# Online Regex tester and debugger : https://regex101.com/
# Regex Demystified: https://www.youtube.com/playlist?list=PL55RiY5tL51ryV3MhCbH8bLl7O_RZGUUE
# NOTE: there are few more metacharacters which I have purposefully left as
# don't offer much value compared to performance disadvantage that comes with it
# eg. backreferences, negative and positive look-aheads, you can explore them
# here: https://realpython.com/regex-python/#metacharacters-supported-by-the-re-module
# more: https://realpython.com/regex-python/#modified-regular-expression-matching-with-flags
