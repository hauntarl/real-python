import time
from concurrent.futures import ThreadPoolExecutor


def calculate(limit):
    return sum(i * i for i in range(limit))


def find_sums(numbers):
    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(calculate, numbers)


if __name__ == '__main__':
    numbers = [5_000_000 + x for x in range(20)]
    print('Starting calculation')
    start = time.monotonic()
    find_sums(numbers)
    duration = time.monotonic() - start
    print(f'Finished computations in {duration:.2f} seconds')
