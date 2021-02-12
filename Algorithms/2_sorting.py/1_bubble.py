def bubble(items: list):
    '''
    - basic idea: move the largest element in the list to the end of the list,
      then second-largest to the second-last position and so on...
    - named because the element in question "bubbles" to the top of the list in
      a series of swaps with adjacent elements

    to run the doctest: python -m doctest file_name.py
    >>> bubble([1, 2, 5, 2, 3, 8, 1])
    [1, 1, 2, 2, 3, 5, 8]
    >>> bubble([1, 2, 3, 4, 5, 6, 7])
    [1, 2, 3, 4, 5, 6, 7]
    >>> bubble([7, 6, 5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5, 6, 7]
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
