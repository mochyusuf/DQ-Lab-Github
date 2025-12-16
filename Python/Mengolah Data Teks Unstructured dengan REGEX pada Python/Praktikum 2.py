#Import library yang dibutuhkan
import pandas as pd

#Baca file dqlabregex.tsv
dqlabregex = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dqlabregex.tsv", sep = '\t')

#Buat kolom baru char_nonnumerik untuk mengetahui jumlah_member non numerik
dqlabregex['char_nonnumerik'] = dqlabregex['jumlah_member'].str.contains('[^0-9]')
print(dqlabregex[['jumlah_member','char_nonnumerik']])