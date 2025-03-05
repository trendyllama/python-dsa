"""
- sorting functions module
"""

from collections.abc import Callable, Iterable


def is_greater_than(element1: int | float, element2: int | float) -> bool:
    return element1 < element2


def is_less_than(element1: int | float, element2: int | float) -> bool:
    return element1 > element2


def bubble_sort(arr: Iterable, comparison_function: Callable) -> Iterable:
    """
    - codecademy implementation of bubble sort
    """
    swaps = 0

    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for idx in range(len(arr) - 1):
            if comparison_function(arr[idx], arr[idx + 1]):
                is_sorted = False
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
                swaps += 1
    print(f"Bubble sort: There were {swaps} swaps")

    return arr


def bubble_sort2(
    arr: Iterable, comparison_function: Callable
) -> Callable | Iterable:
    """
    - not correct yet
    """

    for idx in range(len(arr) - 1):
        if comparison_function(arr[idx], arr[idx + 1]):
            arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

            return bubble_sort2(arr=arr, comparison_function=comparison_function)

    return arr
