def swap(arr: list, index_1: int, index_2: int) -> list:
    """
    Examples:
    >>> swap([1, 2, 3], 0, 1)
    [2, 1, 3]
    >>> swap([3, 2, 1], 0, 2)
    [1, 2, 3]
    >>> swap([1, 3, 2], 1, 2)
    [1, 2, 3]
    """
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp

    return arr


def bubble_sort(arr: list) -> list:
    """
    Examples:
    >>> bubble_sort([1, 2, 3])
    [1, 2, 3]
    >>> bubble_sort([3, 2, 1])
    [1, 2, 3]
    >>> bubble_sort([1, 3, 2])
    [1, 2, 3]

    """
    for idx1, _ in enumerate(arr):
        for idx2 in range(len(arr) - idx1 - 1):
            if arr[idx2] > arr[idx2 + 1]:
                swap(arr, idx2, idx2 + 1)

    return arr
