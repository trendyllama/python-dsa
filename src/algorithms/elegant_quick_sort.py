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

    if len(list_input) <= 1:
        return list_input

    pivot = list_input[-1]

    smaller = [x for x in list_input[:-1] if x <= pivot]
    larger = [x for x in list_input[:-1] if x > pivot]

    return quick_sort(smaller) + [pivot] + quick_sort(larger)
