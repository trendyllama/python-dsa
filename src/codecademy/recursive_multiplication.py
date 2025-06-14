from functools import cache


@cache
def multiplication(n, m):
    """

    Example:
    >>> multiplication(3, 7)
    21
    >>> multiplication(5, 5)
    25
    >>> multiplication(0, 4)
    0
    """
    # base case
    if n == 0 or m == 0:
        return 0
    return n + multiplication(n, m - 1)


@cache
def recursive_sum(n: int, m: int) -> int:
    """
    Example:
    >>> recursive_sum(1, 2)
    3
    >>> recursive_sum(5, 7)
    12
    >>> recursive_sum(30, 12)
    42
    """

    if n == 0:
        return m

    return recursive_sum(n - 1, m + 1)
