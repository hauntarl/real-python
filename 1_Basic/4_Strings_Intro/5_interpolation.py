# interpoalting variables into string

# the ugly way
n, m = 20, 25
prod = n * m
print('The product of', n, 'and', m, 'is', prod)

# the good looking way
print(f'The product of {n} and {m} is {n * m}')

# you can create the f-string by either using the 
# lowercase 'f' or uppercase 'F' and also with
# double and triple quotes syntax
