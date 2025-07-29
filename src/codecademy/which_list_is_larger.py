from functools import reduce


def larger_sum(lst1: list[int], lst2: list[int]) -> tuple[int, list[int], int]:
    """
    Example:
    >>> larger_sum([1, 2, 3], [4, 5])
    (2, [4, 5], 9)
    >>> larger_sum([10, 20, 30], [5, 15])
    (1, [10, 20, 30], 60)
    >>> larger_sum([1, 2], [3, 4, 5])
    (2, [3, 4, 5], 12)
    """
    sum1 = reduce(lambda x, y: x + y, lst1)

    sum2 = reduce(lambda x, y: x + y, lst2)

    return (
        1 if sum1 > sum2 else 2,
        lst1 if sum1 > sum2 else lst2,
        sum1 if sum1 > sum2 else sum2,
    )
