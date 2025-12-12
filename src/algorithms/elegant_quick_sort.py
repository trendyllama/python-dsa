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

    >>> quick_sort([3, 6, 8, 10, 1, 2, 1])
    [1, 1, 2, 3, 6, 8, 10]
    >>> quick_sort([10, 7, 8, 9, 1, 5])
    [1, 5, 7, 8, 9, 10]
    >>> quick_sort([3, 6, 8, 10, 1, 2, 1])
    [1, 1, 2, 3, 6, 8, 10]
    """

    if len(list_input) <= 1:
        return list_input

    pivot = list_input[-1]

    smaller = list(filter(lambda x: x <= pivot, list_input[:-1]))
    larger = list(filter(lambda x: x > pivot, list_input[:-1]))

    return [*quick_sort(smaller), pivot, *quick_sort(larger)]
