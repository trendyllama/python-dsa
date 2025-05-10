from operator import gt, le


def quick_sort(list_input: list) -> list:
    """
    - most elegant implementation of quicksort

    Examples:
    >>> quick_sort([3, 2, 1])
    [1, 2, 3]
    >>> quick_sort([1, 2, 3])
    [1, 2, 3]
    >>> quick_sort([1, 3, 2])
    [1, 2, 3]
    """

    if le(len(list_input), 1):
        return list_input

    pivot = list_input[-1]

    smaller = list(filter(lambda x: le(x, pivot), list_input[:-1]))
    larger = list(filter(lambda x: gt(x, pivot), list_input[:-1]))

    return quick_sort(smaller) + [pivot] + quick_sort(larger)
