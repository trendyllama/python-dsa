import io
import logging
import time
from contextlib import contextmanager

import pandas as pd
import requests

logger = logging.getLogger(__name__)


@contextmanager
def timed_context():
    start_time = time.perf_counter()
    yield
    end_time = time.perf_counter()
    logger.info("%s took %.4f seconds to complete.", end_time - start_time)


def _display_iris():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/iris.csv"

    response = requests.get(url)

    response.raise_for_status()

    with timed_context():

        df = pd.read_csv(io.BytesIO(response.content))

    return df


def _test_display_iris():
    df = _display_iris()

    assert df is not None
    assert not df.empty, "DataFrame is empty"
    assert df.shape[1] == 5, "DataFrame does not have 5 columns"
    assert list(df.columns) == [
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width",
        "species",
    ], "DataFrame does not have the expected column names"


def _display_imdb_reviews():
    url = "https://raw.githubusercontent.com/SkyThonk/Movie-Reviews-Sentiment-Analysis/refs/heads/master/dataset/IMDB%20Dataset.csv"

    response = requests.get(url)
    response.raise_for_status()

    content = io.BytesIO(response.content)

    with timed_context():
        _ = pd.read_csv(content, encoding="utf-8", engine="pyarrow")

    content = io.BytesIO(response.content)

    with timed_context():
        _ = pd.read_csv(content, encoding="utf-8")


if __name__ == "__main__":
    _display_imdb_reviews()
