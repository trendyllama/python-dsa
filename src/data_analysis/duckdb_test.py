import io
import logging

import duckdb
import pandas as pd
import requests

logger = logging.getLogger(__name__)


def main():
    url = "https://raw.githubusercontent.com/SkyThonk/Movie-Reviews-Sentiment-Analysis/refs/heads/master/dataset/IMDB%20Dataset.csv"
    r = requests.get(url)

    r.raise_for_status()

    content = io.BytesIO(r.content)
    # Read the CSV file into a DataFrame
    df = pd.read_csv(
        content, encoding="utf-8", engine="pyarrow", dtype_backend="pyarrow"
    )

    duckdb.register("data_view", df)

    filtered = duckdb.query("select * from data_view where sentiment = 'positive'")

    logger.info(filtered)

    connection = duckdb.connect(database=":memory:")

    cursor = connection.cursor()
    negative = cursor.execute(
        """select review
            from df
            where sentiment = \'negative\'
            """
    )

    positive = cursor.execute("""

    select review from df where sentiment = 'positive'
    """)

    logger.info(positive)

    logger.info(negative)


if __name__ == "__main__":
    main()
