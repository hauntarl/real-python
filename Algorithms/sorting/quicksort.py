from random import randint
from timer import timed


def sort(items, low, high):
    '''
    . basic idea: choose a pivot element, then divide the list into three 
      sections -> elements that are less-than, equal to, greater-than the pivot
      element
    . call quick-sort recursively on the less-than and greater-than sublist

    Caveats with pivot as the 1st element
    . worst-case runtime of quicksort can be O(n^2), this happens when the list
      is already sorted, only if you have chosen your pivot as the first element
    . you can also run into stack overflow error, if the size of the elements 
      is huge (eg. 1,000,000 items) and the list is already sorted, the 
      algorithm will recursively call itself for number of items times, which 
      can cause out of memory issues.

    Better pivot
    . if you choose a random item from the list, everytime you call the 
      function, the random choice in vast majority of cases will choose an 
      item that's farther away from the bottom or the top of the random array
    . there are also other ways that you can choose pivot, making few different
      random choices and taking a median or mean of those

    Three-way Partition
    . quick sort can be inplace as well, in order to reduce space complexity
      using inplace sorting and have support for duplicate elements you need to
      perform three-way partition as follows
    '''
    if low >= high:
        return items

    pivot = items[randint(low, high)]  # selecting a pivot
    # initialize variables for partition
    left = low    # [low, left) - less than elements
    right = low   # [left, right) - equal to pivot
    upper = high  # [right, upper] - unexamined, (upper, high] - greater than
    while right <= upper:
        if items[right] < pivot:
            items[left], items[right] = items[right], items[left]
            left += 1
            right += 1
        elif items[right] > pivot:
            items[right], items[upper] = items[upper], items[right]
            upper -= 1
        else:
            right += 1

    sort(items, low, left-1)
    sort(items, right, high)
    return items


@timed
def to_sort(items): sort(items, 0, len(items) - 1)


# Testing
items = [randint(1, 10) for _ in range(10)]
print(items)
print(sort(items, 0, len(items) - 1))

# Benchmarking: to test how scalable the algorithm is
# to_sort([randint(1, 1000) for _ in range(1000)])
# to_sort([randint(1, 1000) for _ in range(10000)])
