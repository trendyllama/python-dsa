import logging
import time
from functools import wraps

import numpy as np
import pandas as pd
import pyarrow as pa

logger = logging.getLogger(__name__)


def perf_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        s = time.perf_counter()
        result = func(*args, **kwargs)
        e = time.perf_counter()
        logger.info("Function %s took %.4f seconds to run.", func.__name__, e - s)
        return result

    return wrapper


@perf_timer
def _display_pyarrow():
    arrow_table = pa.table([np.random.rand(1000, 3)], names=["A", "B", "C"])

    logger.info("PyArrow table:")
    logger.info(arrow_table)


@perf_timer
def _display_pandas():
    # Create a Pandas DataFrame from the NumPy array
    df = pd.DataFrame(
        [
            np.random.randint(0, 100, 1000),
            np.random.randint(0, 100, 1000),
            np.random.rand(0, 100, 1000),
        ],
        columns=["A", "B", "C"],
    )
    logger.info(df.dtypes)

    logger.info(df)


def main():
    _display_pyarrow()
    _display_pandas()


if __name__ == "__main__":
    main()
