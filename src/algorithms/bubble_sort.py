"""
i dont like that this does these operations in place
"""

NUMS = [5, 2, 9, 1, 5, 6]


def swap(arr: list, index_1: int, index_2: int) -> list:
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp

    return arr


def bubble_sort(arr: list) -> list:
    for idx1, _ in enumerate(arr):
        for idx2 in range(len(arr) - idx1 - 1):
            if arr[idx2] > arr[idx2 + 1]:
                swap(arr, idx2, idx2 + 1)

    return arr


# test statements
print(f"Pre-Sort: {NUMS}")

bubble_sort(NUMS)

print(f"Post-Sort: {NUMS}")
