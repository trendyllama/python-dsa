"""
i dont like that this does these operations in place
"""

from typing import Iterable


NUMS = [5, 2, 9, 1, 5, 6]


def swap(arr: Iterable, index_1: int, index_2: int) -> Iterable:

    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp

    return arr


def bubble_sort(arr: Iterable) -> Iterable:

    for i in enumerate(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)

    return arr


# test statements
print(f"Pre-Sort: {NUMS}")

bubble_sort(NUMS)

print(f"Post-Sort: {NUMS}")
