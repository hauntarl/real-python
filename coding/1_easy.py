def majority_element_indices(lst):
    '''
    Given a list, find the majority element indices.
    For an element to be a majority, it needs to satisfy:
    m > floor(n / 2)
    where m = count of element,
          n = length of the list

    Doctests for the same
    to run the doctest use: python -m doctest easy.py
    >>> majority_element_indices([1, 1, 2])
    [0, 1]
    >>> majority_element_indices([1, 2])
    []
    >>> majority_element_indices([])
    []
    '''
    # 1. if the list is empty or None, return
    if not lst:
        return []

    from collections import Counter

    # 2. count the occurrence of each element
    elements = Counter(lst)  # O(n)

    # 3. find the element with highest count
    major = max(elements, key=lambda i: elements[i])  # O(n)

    # 4. get indices for the element with highest count
    indices = [i for i, val in enumerate(lst) if val == major]  # O(n)

    # 5. return indices if they satisfy majority condition
    return indices if len(indices) > len(lst) // 2 else []  # O(n)
