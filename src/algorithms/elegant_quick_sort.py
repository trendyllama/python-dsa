from typing import Any


def quick_sort(list_input: list[Any]) -> list[Any]:
    """
    - most elegant implementation of quicksort
    """

    if len(list_input) <= 1:
        return list_input

    pivot = list_input[-1]

    # remove pivot from list without mutation
    list_input = list(filter(lambda x: x != pivot, list_input))

    smaller = list(filter(lambda x: x < pivot, list_input))
    larger = list(filter(lambda x: x > pivot, list_input))

    return quick_sort(smaller) + [pivot] + quick_sort(larger)
