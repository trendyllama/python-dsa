from random import randrange
from collections.abc import Callable


def quicksort(
    list_input: list, start: int, end: int, comparision_func: Callable | None = None
) -> None:
    """
    - inelegant implementation of quicksort

    Examples:
    """

    # this portion of list has been sorted
    if start >= end:
        return
    print(f"Running quicksort on {list_input[start: end + 1]}")

    # select random element to be pivot
    pivot_idx = randrange(start, end + 1)
    pivot_element = list_input[pivot_idx]
    print(f"Selected pivot {pivot_element}")

    # swap random element with last element in sub-lists
    list_input[end], list_input[pivot_idx] = list_input[pivot_idx], list_input[end]

    # tracks all elements which should be to left (lesser than) pivot
    less_than_pointer = start

    for i in range(start, end):
        # we found an element out of place
        if list_input[i] < pivot_element:
            # swap element to the right-most portion of lesser elements
            print(f"Swapping {list_input[i]} with {list_input[less_than_pointer]}")
            list_input[i], list_input[less_than_pointer] = (
                list_input[less_than_pointer],
                list_input[i],
            )
            # tally that we have one more lesser element
            less_than_pointer += 1
    # move pivot element to the right-most portion of lesser elements
    list_input[end], list_input[less_than_pointer] = (
        list_input[less_than_pointer],
        list_input[end],
    )
    print(f"{list_input[start: end + 1]} successfully partitioned")
    # recursively sort left and right sub-lists
    quicksort(list_input, start, less_than_pointer - 1)
    quicksort(list_input, less_than_pointer + 1, end)
