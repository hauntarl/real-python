t = ('egg', 'bacon', 'spam', 'tomato')
# unpacking
s1, s2, s3, s4 = t
# while unpacking, you need to have the same number of objects on left side
# as the values in the tuples, else it raises ValueError
print(s1, s2, s3, s4)

# packing and unpacking can be done in one stage
s1, s2, s3, s4 = ('egg', 'bacon', 'spam', 'tomato')
print(s1, s2, s3, s4)
# NOTE: both sides can have parenthesis or can completely omit them
t = 'egg', 'bacon', 'spam', 'tomato'
print(t)

# swapping elements in python using the tuple assignment
a = 'egg'
b = 'bacon'
print(a, b)
a, b = b, a
print(a, b)

# fibonacci in python
a, b = 0, 1
result = []
while a < 20:
    result.append(a)
    a, b = b, a + b
print(result)
