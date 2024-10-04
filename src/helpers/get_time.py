"""
- helper functions
"""

import time
from collections.abc import Callable


def get_time(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        s = time.time()

        res = func(*args, **kwargs)

        elp = time.time() - s

        print(f"{func.__name__} executed in {elp} seconds")

        return res

    return wrapper


@get_time
def test_func() -> None:
    count = 0

    for i in range(1, 100000):
        count += i


if __name__ == "__main__":
    test_func()
