# list of operators...
# ==, !=, <, <=, >, >=
# Comparison operators are typically used in Boolean contexts 
# like conditional and loop statements to direct program flow
a = 10
b = 10
print(a, b)
print('a == b ?', a == b)
print('a != b ?', a != b)
print('a < b ?', a < b)
print('a <= b ?', a <= b)
print('a > b ?', a > b)
print('a >= b ?', a >= b)


print('\nEQUALITY IN FLOATING-POINT:')
x = 1.1 + 2.2
print('x = 1.1 + 2.2')
print('x == 3.3 ?', x == 3.3)  # results in false
# creating an acceptable deviation value
# 2 values are equal when the difference is less than the 
# specified tolerance value 
tolerance = .00001
print('|x - 3.3| < 0.00001 ?', abs(x - 3.3) < tolerance)
