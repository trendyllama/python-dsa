from src.algorithms.bubble_sort import bubble_sort

from src.sorted_tale.sorts import (
    bubble_sort as bubble_sort3,
    is_greater_than,
    bubble_sort2,
    is_less_than,
)


def test_bubble_sort():
    assert bubble_sort([3, 6, 2, 9]) == [2, 3, 6, 9]


def test_bubble_sort2():
    assert bubble_sort2([3, 6, 2, 9], is_less_than) == [2, 3, 6, 9]

    assert bubble_sort2([3, 6, 2, 9], is_greater_than) == [9, 6, 3, 2]


def test_bubble_sort3():
    assert bubble_sort3([3, 6, 2, 9], is_less_than) == [2, 3, 6, 9]

    assert bubble_sort3([3, 6, 2, 9], is_greater_than) == [9, 6, 3, 2]
