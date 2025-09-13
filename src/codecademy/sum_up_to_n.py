from functools import lru_cache, reduce


@lru_cache(maxsize=10)
def sum_to_n(n):
    """
    Example:
    >>> sum_to_n(4)
    10
    >>> sum_to_n(5)
    15
    >>> sum_to_n(20)
    210
    >>> sum_to_n(100)
    5050
    """
    if n == 0:
        return 0
    else:
        return n + sum_to_n(n - 1)


@lru_cache(maxsize=10)
def sum_to_n_functional(n: int) -> int:
    """
    Example:
    >>> sum_to_n_functional(4)
    10
    >>> sum_to_n_functional(5)
    15
    >>> sum_to_n_functional(20)
    210
    >>> sum_to_n_functional(100)
    5050
    """

    sum_out = reduce(lambda x, y: x + y, range(n + 1))

    return sum_out
