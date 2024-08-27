"""
- sorting functions module
"""

from typing import Callable, Iterable, Union


def is_greater_than(element1: Union[int, float], element2: Union[int, float]) -> bool:

    return element1 < element2


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
) -> Union[Callable, Iterable]:
    """
    - not correct yet
    """

    for idx in range(len(arr) - 1):

        if comparison_function(arr[idx], arr[idx + 1]):
            arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]

            return bubble_sort(arr=arr, comparison_function=comparison_function)

    return arr
