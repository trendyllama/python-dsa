import io
import logging
import time

import pandas as pd
import requests

logger = logging.getLogger(__name__)


def _display_iris():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/iris.csv"

    request = requests.get(url)

    if request.status_code == 200:
        s = time.perf_counter()
        df = pd.read_csv(io.BytesIO(request.content))

        e = time.perf_counter()
        logger.info("Function took %.4f seconds to run.", e - s)
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

    s = time.perf_counter()
    _ = pd.read_csv(content, encoding="utf-8", engine="pyarrow")
    logger.info("Function took %.4f seconds to run.", time.perf_counter() - s)

    content = io.BytesIO(response.content)
    s = time.perf_counter()
    _ = pd.read_csv(content, encoding="utf-8")
    logger.info("Function took %.4f seconds to run.", time.perf_counter() - s)


if __name__ == "__main__":
    _display_imdb_reviews()
