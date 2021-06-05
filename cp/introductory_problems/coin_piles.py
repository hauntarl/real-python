from util import timeit


@timeit
def coin_piles(t: tuple) -> str:
    """
    [Medium] https://cses.fi/problemset/task/1754
    [Solution] https://cses.fi/paste/61697edb44edc7a922cce0/

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
    return 'YES' if sum(t) % 3 == 0 and max(t) <= 2*min(t) else 'NO'


if __name__ == '__main__':
    coin_piles((0, 0))
    coin_piles((0, 3))
    coin_piles((1, 1))
    coin_piles((1, 2))
    coin_piles((3, 3))
    coin_piles((6, 6))
    coin_piles((2, 4))
    coin_piles((3, 6))
    coin_piles((4, 8))
    coin_piles((11, 4))
''' terminal
run coin_piles((0, 0))
got YES in 0.0000452000 secs.

run coin_piles((0, 3))
got NO in 0.0000141000 secs.

run coin_piles((1, 1))
got NO in 0.0000253000 secs.

run coin_piles((1, 2))
got YES in 0.0000285000 secs.

run coin_piles((3, 3))
got YES in 0.0000277000 secs.

run coin_piles((6, 6))
got YES in 0.0000147000 secs.

run coin_piles((2, 4))
got YES in 0.0000524000 secs.

run coin_piles((3, 6))
got YES in 0.0000151000 secs.

run coin_piles((4, 8))
got YES in 0.0000137000 secs.

run coin_piles((11, 4))
got NO in 0.0000144000 secs.
'''
