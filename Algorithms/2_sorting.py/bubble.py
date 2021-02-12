from timer import timed
from random import randint


@timed
def bubble(items: list):
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


# Benchmarking:
bubble([randint(1, 1000) for _ in range(1000)])
bubble([randint(1, 1000) for _ in range(10000)])
