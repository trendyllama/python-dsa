"""
i dont like that this does these operations in place
"""

from typing import Any

NUMS = [5, 2, 9, 1, 5, 6]


def swap(arr: list[Any], index_1: int, index_2: int) -> list[Any]:
    """_summary_

    Args:
        arr (list[Any]): _description_
        index_1 (int): _description_
        index_2 (int): _description_

    Returns:
        list[Any]: _description_
    """
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp

    return arr


def bubble_sort(arr: list[Any]) -> list[Any]:
    """_summary_

    Args:
        arr (list[Any]): _description_

    Returns:
        list[Any]: _description_
    """
    # swap_indexes = filter(lambda x, y: arr[x] > arr[y + 1], range(len(arr)), range(len(arr) - 1))
    # arr = map(lambda x, y: swap(arr, x, y + 1) if arr[x] > arr[y + 1], range(len(arr)), range(len(arr) - 1))
    for idx1, val1 in enumerate(arr):
        for idx2 in range(len(arr) - 1):
            if arr[idx1] > arr[idx2 + 1]:
                swap(arr, idx1, idx2 + 1)

    return arr


# test statements
print(f"Pre-Sort: {NUMS}")

bubble_sort(NUMS)

print(f"Post-Sort: {NUMS}")
