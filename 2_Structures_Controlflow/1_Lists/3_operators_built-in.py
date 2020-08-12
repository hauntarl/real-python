# operators:
# in operator, membership operator
# returns True if first operand is contained within the second
# else returns False, can be written as not in

a = ['spam', 'egg', 'bacon', 'tomato', 'ham', 'lobster']
print(f'a = {a}')
print(f"Is 'spam' in a? {'spam' in a}")
print(f"Is 'sausage' not in a? {'sausage' not in a}")


# Concatenation(+)
a = ['spam', 'egg', 'bacon', 'tomato']
print(f'\n\na = {a}')
b = ['ham', 'lobster']
print(f'b = {b}')
print(f'a + b = {a + b}')

# Replication(*)
print(f'\nb * 3 = {b * 3}')


# built-in functions:
# len() - returns the length of the list
# min() - returns smallest object from the list
# max() - opposite of min()
a = [1, 2, 7, 4, 9, 0]
print(f'\n\na = {a}')
print(f'len(a) = {len(a)}')
print(f'min(a) = {min(a)}')
print(f'max(a) = {max(a)}\n\n')

# in case of strings it compares the ascii/unicode code point 
# for each character until it encounters 2 different characters
# NOTE: you can't intermix the operands of different types in 
# min()/max() functions, if '<'/'>' operators are not supported
# between those instances, it will raise TypeError
a = [1.1, 1]
print(min(a))
a = [1, '1']
# print(max(a))  # raises TypeError
