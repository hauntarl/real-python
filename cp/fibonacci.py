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
    if n < 1:
        return 0

    num1 = pow(1 + sqrt5, n)
    num2 = pow(1 - sqrt5, n)
    den1 = pow(2, n)
    return round((num1 - num2) / (den1 * sqrt5))


# print the first 11 fibonacci numbers
[fibonacci(n) for n in range(11)]

''' terminal
D:\real-python\cp>c:/pypy3.7-v7.3.3-win32/pypy3.exe d:/real-python/cp/fibonacci.py
inp: 0
out: 0
Function 'fibonacci' took 0.0001656000 secs

inp: 1
out: 1
Function 'fibonacci' took 0.0007225000 secs

inp: 2
out: 1
Function 'fibonacci' took 0.0000537000 secs

inp: 3
out: 2
Function 'fibonacci' took 0.0000206000 secs

inp: 4
out: 3
Function 'fibonacci' took 0.0000146000 secs

inp: 5
out: 5
Function 'fibonacci' took 0.0000341000 secs

inp: 6
out: 8
Function 'fibonacci' took 0.0000275000 secs

inp: 7
out: 13
Function 'fibonacci' took 0.0000267000 secs

inp: 8
out: 21
Function 'fibonacci' took 0.0000231000 secs

inp: 9
out: 34
Function 'fibonacci' took 0.0000585000 secs

inp: 10
out: 55
Function 'fibonacci' took 0.0000251000 secs
'''
