from bisect import bisect, bisect_left
from random import randint
from timer import timed


def recursive(val, items, beg, end):
    if beg > end:
        return

    mid = (beg + end) // 2
    return mid if val == items[mid] else \
        (recursive(val, items, beg, mid - 1) if val < items[mid] else
         recursive(val, items, mid + 1, end))


def iterative(val, items, beg, end):
    while beg <= end:
        mid = (beg + end) // 2
        if val < items[mid]:
            end = mid - 1
        elif val > items[mid]:
            beg = mid + 1
        else:
            return mid

    return -1


@timed
def binary_search(callback, val, items):
    return callback(val, items, 0, len(items) - 1)


@timed
def binary_builtin(callback, val, items):
    return callback(items, val)


# Testing
items, val = list(range(1, 11)), randint(1, 10)
print(items, val)
print(binary_search(recursive, val, items))
print(binary_search(iterative, val, items))
# bisect function returns the rightmost index where the item can be inserted
# in order to maintain the sortedness of list
print(binary_builtin(bisect, val, items) - 1)
# bisect_left function returns the leftmost index where the item can be inserted
# in order to maintain the sortedness of list
print(binary_builtin(bisect_left, val, items))
# Similarly there are insort, insort_left functions in bisect module, which will
# actually insert the given element to its appropriate position


# Benchmarking
print()
items, val = [randint(1, 1000) for _ in range(1000)], randint(1, 1000)
binary_search(recursive, val, items)
binary_search(iterative, val, items)
binary_builtin(bisect, val, items)
binary_builtin(bisect_left, val, items)

print()
items, val = [randint(1, 10000) for _ in range(10000)], randint(1, 10000)
binary_search(recursive, val, items)
binary_search(iterative, val, items)
binary_builtin(bisect, val, items)
binary_builtin(bisect_left, val, items)
