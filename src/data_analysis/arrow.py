import numpy as np
import pyarrow as pa
import pandas as pd
from functools import wraps
import time

from .iris import display_iris, display_imdb_reviews


def perf_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        s = time.perf_counter()
        result = func(*args, **kwargs)
        e = time.perf_counter()
        print(f"Function {func.__name__} took {e - s:.4f} seconds to run.")
        return result

    return wrapper


@perf_timer
def display_pyarrow():
    arrow_table = pa.table([np.random.rand(1000, 3)], names=["A", "B", "C"])

    print("PyArrow table:")
    print(arrow_table)


@perf_timer
def display_pandas():
    # Create a Pandas DataFrame from the NumPy array
    df = pd.DataFrame(
        [
            np.random.randint(0, 100, 1000),
            np.random.randint(0, 100, 1000),
            np.random.rand(0, 100, 1000),
        ],
        columns=["A", "B", "C"],
    )
    print(df.dtypes)

    print(df)


def main():
    # display_pyarrow()
    # display_pandas()

    display_iris()

    display_imdb_reviews()


if __name__ == "__main__":
    main()
