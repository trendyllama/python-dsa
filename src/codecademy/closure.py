from typing import Callable, Any


def make_multiplier(factor: float | int) -> Callable[[float | int], float | int]:
    """
    Example:
    >>> times3 = make_multiplier(3)
    >>> times3(10)
    30
    >>> times5 = make_multiplier(5)
    >>> times5(10)
    50
    """

    def multiplier(number: float | int) -> float | int:
        return number * factor

    return multiplier
