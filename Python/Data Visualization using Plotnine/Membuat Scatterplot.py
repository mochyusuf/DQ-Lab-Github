import matplotlib.pyplot as plt
from plotnine import *
import pandas as pd 
df_penduduk = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/datakependudukandki-dqlab.csv')

df_penduduk_luas_jumlah = df_penduduk.groupby(["NAMA KELURAHAN", "LUAS WILAYAH (KM2)"])["JUMLAH"].agg('sum').reset_index()

(ggplot(data=df_penduduk_luas_jumlah)
+ aes(x='JUMLAH', y='LUAS WILAYAH (KM2)')
+ geom_point()
).draw()
plt.show()