"""
test_strategy.py is a test file for testing the strategy pattern.
"""

import random

from src.design_patterns.strategy import BubbleSortStrategy, Context, QuickSortStrategy


def test_sort_strategy():
    """
    Test the strategy pattern. By changing the strategy of the context object,
    we can change the sorting algorithm

    this mkaes the code more flexible and allows us to change
    the sorting algorithm in the future"""
    rand_list = [random.randint(0, 100) for _ in range(10)]

    context = Context(BubbleSortStrategy())

    assert context.execute([3, 2, 1]) == [1, 2, 3]
    assert context.execute(rand_list) == sorted(rand_list)

    context.set_strategy(QuickSortStrategy())

    assert context.execute([3, 2, 1]) == [1, 2, 3]
    assert context.execute(rand_list) == sorted(rand_list)
