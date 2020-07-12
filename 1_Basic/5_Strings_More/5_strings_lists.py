# these methods operate on or return iterables
# iterables: term for sequencial collection of objects
# many of these methods return either list or tuples
# list : enclosed within [] - mutable
# tuple: enclosed within () - immutable

# str.join(<iterable>) - concatenates them
mylist = ['spam', 'egg', 'sausage', 'bacon', 'lobster']
print('; '.join(mylist))
# the target string acts as a separator between the iterables
word = 'lobster'
print(':'.join(word))
# a string is also an iterable, thus the join function iterates
# through each character and joins them using the separator

# str.join() will only accept iterables of type string
mylist2 = ['spam', 23, 'lobster']
# print(', '.join(mylist2))  # raises a TypeError


# str.partition(<sep>) - partitions the string based on the given
# separator, returns a 3-value tuple
# 1st part contains the substring preceding the separator
# 2nd part is the separator itself
# 3rd part is the substring succedding the separator
s = 'egg.spam.egg'
print(s.partition('.')) # partitions on the first occurrence of the separator
# if you use a character that's not in the string
# the last 2 values of tuple are empty
print(s.partition('$'))

# str.rpartition(<sep>) - does the same but in reverse order


# str.split(sep=None, maxsplit=-1) - splits the target string
# delimited by given 'sep', if 'sep' not provided, delimiter is set to whitespace
# maxsplit determines how many occurrences of delimiter should it make the split on
# by default it is set to -1, which means all
s = 'spam \tbacon sausage egg' # whitespaces could be tabs, newlines
print(s)
print(s.split())
s = 'spam.bacon.sausage.egg'
print(s)
print(s.split('.'))
# recurring delimiters
s = 'spam...bacon...sausage...egg'
print(s)
print(s.split('.'))  # this introduces empty string in the list
# which is not the case for whitespace characters like '\n' '\t' or ' '

link = 'www.realpython.com'
print(link)
print(link.split('.', maxsplit=1))

# str.rsplit() - works in same fashion, the only difference is
# it counts the maxsplit from reverse direction


# str.splitlines() - separates a long string based the predefined line separators 
# in python like: \n \t \r \f, etc.
moby = '''Call me Ishmael.
Some years ago- never mind how long precisely-
having little or no money in my purse,
and nothing particular to interest me on shore,
I thought I would sail about a little and see the watery part of the world.
'''
print()
print(moby)
print(moby.splitlines())