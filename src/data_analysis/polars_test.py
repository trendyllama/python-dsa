import io

import numpy as np
import polars as pl
import requests

_url = "https://raw.githubusercontent.com/SkyThonk/Movie-Reviews-Sentiment-Analysis/refs/heads/master/dataset/IMDB%20Dataset.csv"

_r = requests.get(_url)

_r.raise_for_status()


_df = (
    pl.scan_csv(io.BytesIO(_r.content))
    .sql("SELECT review, sentiment FROM self where sentiment = 'negative'")
    .collect()
)
print(_df)

df = pl.DataFrame(np.random.rand(100000, 16)).sql("SELECT column_0, column_4 FROM self WHERE column_0 > 0.9 and column_4 < 0.1")

print(_df.describe())
