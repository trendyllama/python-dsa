"""
- helper functions

"""

import logging
import time
from collections.abc import Callable
from functools import wraps

logger = logging.getLogger(__name__)


def get_time(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        s = time.perf_counter()

        func(*args, **kwargs)

        elp = time.perf_counter() - s

        logger.debug("%s executed in %s seconds", func.__name__, elp)

    return wrapper


@get_time
def test_func() -> None:
    count = 0

    for i in range(1, 100000):
        count += i
