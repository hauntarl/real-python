from random import randint
from timer import timed


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def sort(items):
    '''
    . basic idea: break the list into two halves, sort those havles recursively
      using merge sort, then "merge" the halves together again.
    . relies on the fact that merging two sorted lists is an O(n) operation
    . NOTE: merge sort is stable
    '''
    if items is None or len(items) <= 1:
        return items

    mid = len(items) // 2
    return merge(sort(items[:mid]), sort(items[mid:]))


@timed
def to_sort(items): sort(items)


# Testing
items = [randint(1, 10) for _ in range(10)]
print(items)
print(sort(items))

# Benchmarking: to test how scalable the algorithm is
# to_sort([randint(1, 1000) for _ in range(1000)])
# to_sort([randint(1, 1000) for _ in range(10000)])
