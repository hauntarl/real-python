from random import randint
from timer import timed


def sort(items: list):
    '''
    - basic idea: move the largest element in the list to the end of the list,
      then second-largest to the second-last position and so on...
    - named because the element in question "bubbles" to the top of the list in
      a series of swaps with adjacent elements
    '''
    for i in range(len(items)):
        is_sorted = True
        for j in range(len(items) - i - 1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                is_sorted = False

        if is_sorted:
            break

    return items


@timed
def to_sort(items): sort(items)


# Testing
items = [randint(1, 10) for _ in range(10)]
print(sort(items))

# Benchmarking: to test how scalable the algorithm is
# to_sort([randint(1, 1000) for _ in range(1000)])
# to_sort([randint(1, 1000) for _ in range(10000)])
