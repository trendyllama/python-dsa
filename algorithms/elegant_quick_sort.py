from typing import Iterable

def quick_sort(array: Iterable) -> Iterable:

    if len(array) <= 1:
        return array

    pivot = array[-1]
    smaller = list(filter(lambda x: x < pivot, array))
    larger = list(filter(lambda x: x >= pivot, array))

    return quick_sort(smaller) + [pivot] + quick_sort(larger)


# test statements

print(quick_sort([5, 2, 9, ]))  # [1, 2, 5, 5, 6, 9]

assert quick_sort([5, 2, 9]) == [2, 5, 9]