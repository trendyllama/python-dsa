"""
- testing data structures and algos
"""

import random

from src.algorithms.elegant_quick_sort import quick_sort


def test_quicksort():
    assert quick_sort([3, 6, 2, 9]) == [2, 3, 6, 9]

    RAND_LIST = [random.randint(1, 50) for _ in range(50)]

    assert quick_sort(RAND_LIST) == sorted(RAND_LIST)
