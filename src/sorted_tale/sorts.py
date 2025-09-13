"""
- sorting functions module
"""

from collections.abc import Callable
from typing import Protocol


def is_greater_than(element1: float, element2: float) -> bool:
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


def is_less_than(element1: float, element2: float) -> bool:
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


class BubbleSortMethod(Protocol):
    comparision_function: Callable

    def __init__(self, array: list, comparison_function: Callable) -> None: ...

    @staticmethod
    def swap(array: list, idx1, idx2) -> list: ...

    def sort(self) -> list: ...


class IterativeBubbleSort(BubbleSortMethod):
    def __init__(self, array: list, comparision_function: Callable) -> None:
        self.comparision_function = comparision_function
        self.array = array

    @staticmethod
    def swap(array: list, idx1, idx2) -> list:
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

    def sort(self) -> list:
        swaps = 0
        arr = self.array

        is_sorted = False

        while not is_sorted:
            is_sorted = True
            for idx in range(len(arr) - 1):
                if self.comparision_function(arr[idx], arr[idx + 1]):
                    is_sorted = False
                    arr = swap(arr, idx, idx + 1)
                    swaps += 1

        return arr


class RecursiveBubbleSort(BubbleSortMethod):
    def __init__(self, array: list, comparison_function: Callable) -> None:
        self.array = array
        self.comparision_function = comparison_function

    @staticmethod
    def swap(array: list, idx1, idx2) -> list:
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

    def sort(self) -> list:
        def inner(arr: list):
            for idx in range(len(arr) - 1):
                if self.comparision_function(arr[idx], arr[idx + 1]):
                    arr = swap(arr, idx, idx + 1)

                    return inner(arr)

            return arr

        return inner(self.array)
