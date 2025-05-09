import random
from src.algorithms.bubble_sort import bubble_sort

from src.sorted_tale.sorts import (
    bubble_sort as bubble_sort3,
    is_greater_than,
    bubble_sort2,
    is_less_than,
)


def test_bubble_sort():
    for _ in range(50):
        rand_list = random.sample(range(100), 10)
        assert bubble_sort(rand_list) == sorted(rand_list)


def test_bubble_sort2():
    for _ in range(50):
        rand_list = random.sample(range(100), 10)
        assert bubble_sort2(rand_list, is_less_than) == sorted(rand_list)
        assert bubble_sort2(rand_list, is_greater_than) == sorted(
            rand_list, reverse=True
        )


def test_bubble_sort3():
    for _ in range(50):
        rand_list = random.sample(range(100), 10)
        assert bubble_sort3(rand_list, is_less_than) == sorted(rand_list)
        assert bubble_sort3(rand_list, is_greater_than) == sorted(
            rand_list, reverse=True
        )
