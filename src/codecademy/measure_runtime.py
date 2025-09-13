import functools
import logging
import time

logger = logging.getLogger(__name__)


# decorator to measure running time
def measure_running_time(echo=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            t_1 = time.perf_counter()
            ans = func(*args, **kwargs)
            t_2 = time.perf_counter()
            elp = t_2 - t_1

            if echo:
                logger.info("%s running time is %s s", func.__name__, elp)
            return ans

        return wrapped

    return decorator
