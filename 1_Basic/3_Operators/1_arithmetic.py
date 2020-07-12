a = 10
b = 20
print(a + b)
print(a + b - 5)  # a sequence like a + b - 5 is called an expression

# list of operators...
# + - : (unary/binary)
# * : multiplication, ** : exponential (a ^ b)
# / : division (float), // : division (int)
# % : modulo
# Refer: https://realpython.com/python-operators-expressions/#arithmetic-operators
a = 5
b = 3
print('unary + : ', +a)
print('unary - : ', -b)
print('binary + : ', a + b)
print('binary - : ', a - b)
print('mul * : ', a * b)
print('expo ** : ', a ** b)
print('div / : ', a / b, type(a / b))  # result always float
print('div // : ', a // b, type(a // b))
print('mod % : ', a % b)
