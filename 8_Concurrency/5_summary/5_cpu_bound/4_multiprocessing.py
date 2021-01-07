import time
from multiprocessing import Pool


def calculate(limit):
    return sum(i * i for i in range(limit))


def find_sums(numbers):
    with Pool() as pool:
        pool.map(calculate, numbers)


if __name__ == '__main__':
    numbers = [5_000_000 + x for x in range(20)]
    print('Starting calculation')
    start = time.monotonic()
    find_sums(numbers)
    duration = time.monotonic() - start
    print(f'Finished computations in {duration:.2f} seconds')
