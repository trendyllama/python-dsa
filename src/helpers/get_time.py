"""
- helper functions

"""

import time
from functools import wraps
from collections.abc import Callable


def get_time(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        s = time.perf_counter()

        func(*args, **kwargs)

        elp = time.perf_counter() - s

        print(f"{func.__name__} executed in {elp} seconds")

    return wrapper


@get_time
def test_func() -> None:
    count = 0

    for i in range(1, 100000):
        count += i
