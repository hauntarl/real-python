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
D:\real-python>c:/pypy3.7-v7.3.3-win32/pypy3.exe d:/real-python/cp/fibonacci.py
inp: 0
out: 0
took 0.0000021000 secs

inp: 1
out: 1
took 0.0000651000 secs

inp: 2
out: 1
took 0.0000216000 secs

inp: 3
out: 2
took 0.0000186000 secs

inp: 4
out: 3
took 0.0000198000 secs

inp: 5
out: 5
took 0.0000179000 secs

inp: 6
out: 8
took 0.0000161000 secs

inp: 7
out: 13
took 0.0000158000 secs

inp: 8
out: 21
took 0.0000383000 secs

inp: 9
out: 34
took 0.0000660000 secs

inp: 10
out: 55
took 0.0000178000 secs
'''
