from util import timeit

y, n = 'YES', 'NO'


@timeit
def coin_piles(a: int, b: int) -> str:
    """
    [Medium] https://cses.fi/problemset/task/1754
    [Solution] https://cses.fi/paste/77351c7897fe6a7422cc1c/

    You have two coin piles containing a and b coins. On each move, you can 
    either remove one coin from the left pile and two coins from the right 
    pile, or two coins from the left pile and one coin from the right pile.

    Your task is to efficiently find out if you can empty both the piles.
    The first input line has an integer t: the number of tests.
    After this, there are t lines, each of which has two integers a and b: the 
    numbers of coins in the piles.

    For each test, print "YES" if you can empty the piles and "NO" otherwise.

    Constraints: 
    . 1 ≤ t ≤ 10^5
    . 0 ≤ a, b ≤ 10^9
    """
    a, b = max(a, b), min(a, b)
    c = 2 * b
    if a > c:
        return n
    if a == c:
        return y

    s = a % 3 + b % 3
    return y if s == 0 or s == 3 else n


if __name__ == '__main__':
    coin_piles(0, 0)
    coin_piles(0, 3)
    coin_piles(1, 1)
    coin_piles(1, 2)
    coin_piles(3, 3)
    coin_piles(6, 6)
    coin_piles(2, 4)
    coin_piles(3, 6)
    coin_piles(4, 8)
    coin_piles(11, 4)
''' terminal
run coin_piles(0, 0)
got YES in 0.0000149000 secs.

run coin_piles(0, 3)
got NO in 0.0000085000 secs.

run coin_piles(1, 1)
got NO in 0.0000294000 secs.

run coin_piles(1, 2)
got YES in 0.0000142000 secs.

run coin_piles(3, 3)
got YES in 0.0000389000 secs.

run coin_piles(6, 6)
got YES in 0.0000171000 secs.

run coin_piles(2, 4)
got YES in 0.0000092000 secs.

run coin_piles(3, 6)
got YES in 0.0000089000 secs.

run coin_piles(4, 8)
got YES in 0.0000096000 secs.

run coin_piles(11, 4)
got NO in 0.0001180000 secs.
'''
