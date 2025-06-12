import functools
import time


# decorator to measure running time
def measure_running_time(echo=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            t_1 = time.time()
            ans = func(*args, **kwargs)
            t_2 = time.time()
            if echo:
                print(f"{func.__name__}() running time is {t_2 - t_1:.2f} s")
            return ans

        return wrapped

    return decorator