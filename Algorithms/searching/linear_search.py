from random import randint
from timer import timed


@timed
def linear_search(val, items):
    for i, item in enumerate(items):
        if item == val:
            return i
    return -1


# this will work much faster compared to our implementation because the
# underlying algorithm is written in C, so there is no need to re-invent the
# wheel for linear search
@timed
def linear_builtin(val, items): return items.index(val)


# Testing
items, val = [randint(1, 10) for _ in range(10)], randint(1, 10)
print(items, val)
print(linear_search(val, items))
print(linear_builtin(val, items))

# Benchmarking
print()
items, val = [randint(1, 1000) for _ in range(1000)], randint(1, 1000)
linear_search(val, items)
linear_builtin(val, items)

print()
items, val = [randint(1, 10000) for _ in range(10000)], randint(1, 10000)
linear_search(val, items)
linear_builtin(val, items)
