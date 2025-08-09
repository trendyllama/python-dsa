import duckdb
import pandas as pd

import io
import requests
url = "https://raw.githubusercontent.com/SkyThonk/Movie-Reviews-Sentiment-Analysis/refs/heads/master/dataset/IMDB%20Dataset.csv"
r = requests.get(url)
if r.status_code != 200:
    raise ConnectionError
content = io.BytesIO(r.content)
# Read the CSV file into a DataFrame
df = pd.read_csv(content, encoding="utf-8", engine="pyarrow")
print(df.info())


db = duckdb.connect(database=":memory:")
res = db.execute(
    '''select *
        from df
        where sentiment = 'negative'
        '''
).fetchdf()

print(res)
