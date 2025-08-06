"""
- sorting functions module
"""

from collections.abc import Callable


def is_greater_than(element1: int | float, element2: int | float) -> bool:
    """
    Examples:
    >>> is_greater_than(1, 2)
    True
    >>> is_greater_than(2, 1)
    False
    >>> is_greater_than(1, 1)
    False

    """
    return element1 < element2


def is_less_than(element1: int | float, element2: int | float) -> bool:
    """
    Examples:
    >>> is_less_than(1, 2)
    False
    >>> is_less_than(2, 1)
    True
    >>> is_less_than(1, 1)
    False
    """
    return element1 > element2


def bubble_sort(arr: list, comparison_function: Callable) -> list:
    """
    - codecademy implementation of bubble sort

    Examples:
    >>> bubble_sort([1, 2, 3], is_greater_than)
    [3, 2, 1]
    >>> bubble_sort([3, 2, 1], is_greater_than)
    [3, 2, 1]
    >>> bubble_sort([1, 3, 2], is_greater_than)
    [3, 2, 1]
    >>> bubble_sort([1, 2, 3], is_less_than)
    [1, 2, 3]
    """
    swaps = 0

    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for idx in range(len(arr) - 1):
            if comparison_function(arr[idx], arr[idx + 1]):
                is_sorted = False
                arr = swap(arr, idx, idx + 1)
                swaps += 1

    return arr


def swap(array, idx1, idx2):
    """
    Example:
    >>> lst = [1, 2, 3, 4]
    >>> lst
    [1, 2, 3, 4]
    >>> lst = swap(lst, 1, 2)
    >>> lst
    [1, 3, 2, 4]

    """
    array[idx1], array[idx2] = array[idx2], array[idx1]
    return array


def bubble_sort2(arr: list, comparison_function: Callable) -> Callable | list:
    """
    - not correct yet

    Examples:
    >>> bubble_sort2([1, 2, 3], is_greater_than)
    [3, 2, 1]
    >>> bubble_sort2([3, 2, 1], is_greater_than)
    [3, 2, 1]
    >>> bubble_sort2([1, 3, 2], is_greater_than)
    [3, 2, 1]
    >>> bubble_sort2([1, 2, 3], is_less_than)
    [1, 2, 3]
    """

    for idx in range(len(arr) - 1):
        if comparison_function(arr[idx], arr[idx + 1]):
            arr = swap(arr, idx, idx + 1)

            return bubble_sort2(arr=arr, comparison_function=comparison_function)

    return arr
