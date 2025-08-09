

import io
import polars as pl
import requests
import numpy as np

url = "https://raw.githubusercontent.com/SkyThonk/Movie-Reviews-Sentiment-Analysis/refs/heads/master/dataset/IMDB%20Dataset.csv"

r = requests.get(url)

if r.status_code != 200:
    raise ConnectionError

df = pl.read_csv(io.BytesIO(r.content), encoding="utf-8").sql("SELECT * FROM self where sentiment = 'negative'")

df = pl.DataFrame(np.random.rand(100000, 16)).sql("SELECT column_0, column_4 FROM self WHERE column_0 > 0.9 and column_4 < 0.1")

print(df)
print(df.describe())
