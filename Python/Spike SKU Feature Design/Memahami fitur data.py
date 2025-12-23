# Import library Pandas
import pandas as pd

# Baca dataset “funnel.csv”
df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/komdigi/tbl_funnel.csv")

# Tampilkan dataframe tersebut.
print(df)