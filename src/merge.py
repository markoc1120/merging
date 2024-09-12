"""Code for merging two sorted lists."""

from collections import deque


def merge(x: list[int], y: list[int]) -> list[int]:
    """
    Merge two sorted lists.

    Returns a list that contains all the elements in x and y
    in sorted order.

    >>> merge([1, 2, 4, 6], [1, 3, 4, 5])
    [1, 1, 2, 3, 4, 4, 5, 6]
    """
    x, y = deque(x), deque(y)
    ans = []
    while x and y:
        if x[0] < y[0]:
            ans.append(x.popleft())
        else:
            ans.append(y.popleft())
    if x:
        ans.extend(x)
    elif y:
        ans.extend(y)
    return ans
