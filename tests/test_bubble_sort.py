import random
import unittest

from src.algorithms.bubble_sort import bubble_sort
from src.sorted_tale.sorts import (
    BubbleSortMethod,
    IterativeBubbleSort,
    RecursiveBubbleSort,
    bubble_sort2,
    is_greater_than,
    is_less_than,
)
from src.sorted_tale.sorts import (
    bubble_sort as bubble_sort3,
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


class TestBubbleSortClasses(unittest.TestCase):

    def setUp(self) -> None:

        self.sort_methods: list[type[BubbleSortMethod]] = [
            RecursiveBubbleSort,
            IterativeBubbleSort
        ]

        self.comparison_functions = [
            is_greater_than,
            is_less_than
        ]


    def test_methods_with_less_than(self):

        rand_list = random.sample(range(100), 10)

        for method in self.sort_methods:

            method = method(rand_list, is_less_than)

            assert method.sort() == sorted(rand_list)

    def test_methods_with_grater_then(self):
        rand_list = random.sample(range(100), 10)

        for method in self.sort_methods:

            method = method(rand_list, is_greater_than)

            assert method.sort() == sorted(rand_list, reverse=True)
