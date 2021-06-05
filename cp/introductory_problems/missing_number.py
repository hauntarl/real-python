from util import timeit


@timeit
def missing_number(n: str, terms: str) -> int:
    """
    [Easy] https://cses.fi/problemset/task/1083/
    [Solution] https://cses.fi/paste/e83a55e0c5f903922194a9/

    You are given all numbers between 1,2,…,n except one. Your task is to find 
    the missing number.

    Print the missing number.

    Constraints: 2 ≤ n ≤ 2 * 10^5
    """
    n = int(n)
    s = n * (n + 1) >> 1
    for v in terms.split(' '):
        s -= int(v)
    return s


if __name__ == '__main__':
    missing_number('10', '2 8 10 6 5 1 3 7 4')
    missing_number('100', '27 4 16 47 24 38 61 94 98 79 22 50 75 89 64 78 9 10 30 76 73 58 21 37 44 70 60 45 12 92 84 34 25 57 90 96 69 20 97 87 67 65 83 33 40 74 95 39 100 48 53 59 19 1 28 66 72 54 68 2 32 91 86 6 13 62 81 5 17 77 41 35 99 14 80 56 36 31 29 85 7 11 8 93 15 88 43 3 52 82 51 26 55 63 42 23 49 46 18')
''' terminal
run missing_number('10', '2 8 10 6 5 1 3 7 4')
got 9 in 0.0000225000 secs.

run missing_number('100', '27 4 16 47 24 38 61 94 98 79 22 50 75 89 64 78 9 10 30 76 73 58 21 37 44 70 60 45 12 92 84 34 25 57 90 96 69 20 97 87 67 65 83 33 40 74 95 39 100 48 53 59 19 1 28 66 72 54 68 2 32 91 86 6 13 62 81 5 17 77 41 35 99 14 80 56 36 31 29 85 7 11 8 93 15 88 43 3 52 82 51 26 55 63 42 23 49 46 18')
got 71 in 0.0001980000 secs.
'''
