import random
from typing import Iterable

def quick_sort(list_input: Iterable) -> Iterable:

    if len(list_input) <= 1:
        return list_input

    pivot = list_input[-1]

    # remove pivot from list without mutation
    list_input = list(filter(lambda x: x != pivot, list_input))

    smaller = list(filter(lambda x: x < pivot, list_input))
    larger = list(filter(lambda x: x >= pivot, list_input))

    return quick_sort(smaller) + [pivot] + quick_sort(larger)


# test statements
RAND_LIST = [random.randint(1, 50) for _ in range(50)]

print(RAND_LIST)
print(quick_sort(RAND_LIST)) # weird that this removed duplicates

print(sorted(RAND_LIST))
# assert quick_sort(RAND_LIST) == sorted(RAND_LIST)