"""
- testing data structures and algos
"""

import random

import pytest

from src.algorithms.elegant_quick_sort import quick_sort


@pytest.mark.parametrize("value", list(range(1, 1000)))
def test_quicksort(value: int):
    rand_list = [random.randint(1, 50) for _ in range(value)]

    assert quick_sort(rand_list) == sorted(rand_list)
