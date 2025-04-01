def quick_sort(list_input: list) -> list:
    """
    - most elegant implementation of quicksort
    """

    if len(list_input) <= 1:
        return list_input

    pivot = list_input[-1]

    smaller = [x for x in list_input[:-1] if x <= pivot]
    larger = [x for x in list_input[:-1] if x > pivot]

    return quick_sort(smaller) + [pivot] + quick_sort(larger)
