"""
test_strategy.py is a test file for testing the strategy pattern.
"""

import random

import pytest

from src.design_patterns.strategy import (
    BubbleSortStrategy,
    Context,
    DefaultSortStrategy,
    QuickSortStrategy,
)


@pytest.mark.parametrize(
    ("strategy", "expected"),
    [
        (BubbleSortStrategy(), [1, 2, 3]),
        (QuickSortStrategy(), [1, 2, 3]),
        (DefaultSortStrategy(), [1, 2, 3]),
    ],
)
def test_sort_strategy_with_parametrize(strategy, expected):
    """
    Test the strategy pattern. By changing the strategy of the context object,
    we can change the sorting algorithm

    this makes the code more flexible and allows us to change
    the sorting algorithm in the future"""
    rand_list = [random.randint(0, 100) for _ in range(10)]

    context = Context(strategy)

    assert context.execute([3, 2, 1]) == expected
    assert context.execute(rand_list) == sorted(rand_list)
