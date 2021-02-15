from random import randint
from timer import timed


@timed
def random_search(val, items):
    seen = set()
    while len(seen) < len(items):
        key = randint(0, len(items) - 1)
        if items[key] == val:
            return key
        seen.add(key)

    return -1


items, val = [randint(1, 10) for _ in range(10)], randint(1, 10)
print(items, val)
print(random_search(val, items))
