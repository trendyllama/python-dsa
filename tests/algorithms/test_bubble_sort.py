import random

import pytest

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

length = 10


@pytest.mark.parametrize("length", range(length))
def test_bubble_sort(length: int):
    for _ in range(length):
        rand_list = random.sample(range(100), length)
        assert bubble_sort(rand_list) == sorted(rand_list)


@pytest.mark.parametrize("length", range(length))
def test_bubble_sort2(length: int):
    for _ in range(length):
        rand_list = random.sample(range(100), length)
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


@pytest.fixture(params=[RecursiveBubbleSort, IterativeBubbleSort])
def sort_method(request: pytest.FixtureRequest) -> type[BubbleSortMethod]:
    return request.param


def test_sort_method_with_less_than(sort_method: type[BubbleSortMethod]) -> None:
    rand_list = random.sample(range(100), 10)
    method = sort_method(rand_list, is_less_than)
    assert method.sort() == sorted(rand_list)


def test_sort_method_with_greater_than(sort_method: type[BubbleSortMethod]) -> None:
    rand_list = random.sample(range(100), 10)
    method = sort_method(rand_list, is_greater_than)
    assert method.sort() == sorted(rand_list, reverse=True)
