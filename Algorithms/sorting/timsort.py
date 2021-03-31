'''
. timsort is actually the native sorting algorithm for Python
. it is named after Tim Peters, the person who implemented the algorithm in the
  first place
. when you use "sorted()" function in Python, it actually uses timsort
. the reason being, this algorithm is very fast and in the worst-case it 
  actually is just as fast as the best-case of merge or quick sort, it really
  is a best of both worlds algorithm and a lot more complex to implement
'''
from random import randint
from timer import timed


# modified insertion sort to work on specified sublist of given input
def insertion(items, beg=0, end=None):
    if end is None:
        end = len(items) - 1

    for i in range(beg + 1, end + 1):
        cur = items[i]
        j = i - 1
        while j >= beg and items[j] > cur:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = cur


def merge(left, right):
    i, j = 0, 0
    result = []
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
    - basic idea: divide your list into small sections and use insertion sort
      to sort all those sections, then merge those sections together two at a
      time until the whole list is sorted
    - timsort is an example of a "block merge" sorting algorithm
    - leverages the strength of insertion sort (fast on small lists, stable,
      O(n)) and the strengths of merge sort (improved performance over large 
      lists, O(n log(n)) worst-case performance), while mitigating the weakness
      of both algorithms

    - in practice, merge sort can sometimes be really slow because it has to
      allocate extra space, in fact it always needs to allocate some extra 
      space unless you do some serious work
    '''
    # NOTE: there are various other methods to find optimal bucket size based
    # on given items, for simplicity this algorithm uses a constant literal
    bucket = 64

    for i in range(0, len(items), bucket):
        insertion(items, i, min(i + bucket - 1, len(items) - 1))

    siz = bucket
    while siz < len(items):
        for beg in range(0, len(items), siz * 2):
            mid = beg + siz
            end = min(beg + siz * 2, len(items))
            items[beg: end] = merge(items[beg: mid], items[mid: end])

        siz *= 2

    return items


@timed
def to_sort(items): sort(items)


# Testing
# items = [randint(1, 10) for _ in range(10)]
# print(items)
# print(sort(items))

# Benchmarking:
to_sort([randint(1, 10) for _ in range(10)])
to_sort([randint(1, 1000) for _ in range(1000)])
to_sort([randint(1, 1000) for _ in range(10000)])
