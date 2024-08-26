import random
from typing import Callable, Iterable


def bubble_sort(arr: Iterable, comparison_function: Callable) -> Iterable:
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


def quicksort(
    list_input: Iterable, start: int, end: int, comparison_function: Callable
) -> Iterable:

    if start >= end:
        return

    pivot_idx = random.randrange(start, end + 1)
    pivot_element = list_input[pivot_idx]
    list_input[end], list_input[pivot_idx] = list_input[pivot_idx], list_input[end]
    less_than_pointer = start

    for i in range(start, end):
        if comparison_function(pivot_element, list_input[i]):
            list_input[i], list_input[less_than_pointer] = (
                list_input[less_than_pointer],
                list_input[i],
            )
            less_than_pointer += 1
    list_input[end], list_input[less_than_pointer] = (
        list_input[less_than_pointer],
        list_input[end],
    )

    quicksort(list_input, start, less_than_pointer - 1, comparison_function)
    quicksort(list_input, less_than_pointer + 1, end, comparison_function)
