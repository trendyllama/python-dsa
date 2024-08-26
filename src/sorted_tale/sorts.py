'''
- sorting functions module
'''

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
