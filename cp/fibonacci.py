from util import timeit
from math import sqrt, pow

sqrt5 = sqrt(5)


@timeit
def fibonacci(n: int) -> int:
    """
    There is a closed-form formula for calculating Fibonacci numbers, which is 
    sometimes called Binet’s formula.
    f(n) = ((1 + √5)^n - (1 - √5)^n) / (2^n * √5)
    """
    if n < 0:
        return

    num1 = pow(1 + sqrt5, n)
    num2 = pow(1 - sqrt5, n)
    den1 = pow(2, n)
    return round((num1 - num2) / (den1 * sqrt5))


# print the first 11 fibonacci numbers
[fibonacci(n) for n in range(11)]

''' terminal
D:\real-python\cp>c:/pypy3.7-v7.3.3-win32/pypy3.exe d:/real-python/cp/fibonacci.py
params : 0
result : 0
took 0.0000472000 secs

params : 1
result : 1
took 0.0000225000 secs

params : 2
result : 1
took 0.0000209000 secs

params : 3
result : 2
took 0.0000456000 secs

params : 4
result : 3
took 0.0000148000 secs

params : 5
result : 5
took 0.0000159000 secs

params : 6
result : 8
took 0.0000210000 secs

params : 7
result : 13
took 0.0000174000 secs

params : 8
result : 21
took 0.0000255000 secs

params : 9
result : 34
took 0.0000246000 secs

params : 10
result : 55
took 0.0000242000 secs
'''
