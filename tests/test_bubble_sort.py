from src.algorithms.bubble_sort import bubble_sort


def test_bubble_sort():
    assert bubble_sort([3, 6, 2, 9]) == [2, 3, 6, 9]
