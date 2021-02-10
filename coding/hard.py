class Link:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        if not self.next:
            return f"Link({self.val})"
        return f"Link({self.val}, {self.next})"

    def __gt__(self, other):
        return self.val > other.val


def merge_brute(linked_lists):
    '''
    Merge k sorted linked lists into one
    sorted linked list.
    >>> print(merge_brute([
    ...     Link(1, Link(2)),
    ...     Link(3, Link(4))
    ... ]))
    Link(1, Link(2, Link(3, Link(4))))
    >>> print(merge_brute([
    ...     Link(1, Link(2)),
    ...     Link(2, Link(4)),
    ...     Link(3, Link(3)),
    ... ]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))))
    '''
    # n - number of elements in linked_lists
    # k - total unique elements
    links = []
    for item in linked_lists:  # O(n)
        while item:  # O(k)
            links.append(item.val)
            item = item.next

    links.sort(reverse=True)  # O(nk*Log(nk))
    result = None
    for val in links:  # O(nk)
        result = Link(val, result)

    # final runtime: O(nk*Log(nk))
    return result


def merge_suboptimal(linked_lists):
    '''
    Merge k sorted linked lists into one
    sorted linked list.
    >>> print(merge_suboptimal([
    ...     Link(1, Link(2)),
    ...     Link(3, Link(4))
    ... ]))
    Link(1, Link(2, Link(3, Link(4))))
    >>> print(merge_suboptimal([
    ...     Link(1, Link(2)),
    ...     Link(2, Link(4)),
    ...     Link(3, Link(3)),
    ... ]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))))
    '''
    result = Link(0)
    curr = result

    while any(linked_lists):  # O(nk)
        vals = [link.val for link in linked_lists if link]  # O(n)
        min_val = min(vals)
        for i, link in enumerate(linked_lists):  # O(n)
            if link and link.val == min_val:
                curr.next = Link(link.val)
                curr = curr.next
                linked_lists[i] = link.next

    # final runtime bruteforce: O(nk*Log(nk))
    # final runtime suboptimal: O(nk*n)
    # this solution is relatively slower to the brute force one, unless 'n' is
    # really large to make the value of log(nk) greater than n
    return result.next


def merge_optimal(linked_lists):
    '''
    Merge k sorted linked lists into one
    sorted linked list.
    >>> print(merge_optimal([
    ...     Link(1, Link(2)),
    ...     Link(3, Link(4))
    ... ]))
    Link(1, Link(2, Link(3, Link(4))))
    >>> print(merge_optimal([
    ...     Link(1, Link(2)),
    ...     Link(2, Link(4)),
    ...     Link(3, Link(3)),
    ... ]))
    Link(1, Link(2, Link(2, Link(3, Link(3, Link(4))))))
    '''
    from queue import PriorityQueue

    que = PriorityQueue()
    for link in linked_lists:  # O(n)
        que.put((link.val, link))

    result = Link(0)
    curr = result
    while not que.empty():  # O(k)
        link = que.get()[1]  # O(log(k))
        curr.next = link
        curr = curr.next
        if link.next:
            que.put((link.next.val, link.next))

    # final runtime: O(k*log(k))
    return result.next
