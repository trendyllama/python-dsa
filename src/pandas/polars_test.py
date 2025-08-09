

import io
import polars as pl
import requests

url = "https://raw.githubusercontent.com/SkyThonk/Movie-Reviews-Sentiment-Analysis/refs/heads/master/dataset/IMDB%20Dataset.csv"

r = requests.get(url)

if r.status_code != 200:
    raise ConnectionError

df = pl.read_csv(io.BytesIO(r.content), encoding="utf-8").sql("SELECT * FROM self where sentiment = 'negative'")

print(df)
