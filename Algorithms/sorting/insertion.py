from random import randint
from timer import timed


def sort(items):
    '''
    - basic idea: starting at the second element of the list, move each item
      so that its sorted with respect to all items before it
    - "inserts" each element into its correct place in a sorted sublist that
      grows to become the full list
    '''
    for i in range(1, len(items)):
        cur = items[i]
        pos = i - 1

        while pos >= 0 and items[pos] > cur:
            items[pos+1] = items[pos]
            pos -= 1

        items[pos+1] = cur

    return items


@timed
def to_sort(items): sort(items)


# Benchmarking:
to_sort([randint(1, 1000) for _ in range(1000)])
to_sort([randint(1, 1000) for _ in range(10000)])
