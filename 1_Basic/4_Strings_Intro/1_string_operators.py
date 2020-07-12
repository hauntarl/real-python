# couple of operators used on numeric types can also
# be applied to strings

# + operator: concatenates strings
s = 'spam'
t = 'egg'
u = 'bacon'
print(s + t + u)

# * operator: creates multiple copies of string
print('s * 2', s * 2)  # multiplier needs to be a natural number
print('t * 0', t * 0)  # anything less than 1, it returns empty string
print('u * -1', u * -1)


# in operator: membership operator, returns True if first operand
# is contained within second, else returns False.
stu = 'spam egg bacon'
print('s in stu?', s in stu)
# also can be used as 'not in'
print('t not in stu?', t not in stu)