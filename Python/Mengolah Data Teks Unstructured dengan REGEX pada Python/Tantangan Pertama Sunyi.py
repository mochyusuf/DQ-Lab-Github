#Import library yang dibutuhkan
import pandas as pd

#Baca file dqlabregex.tsv
dqlabregex = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dqlabregex.tsv", sep = '\t')

#Buat kolom baru kota_awalan_J_S
dqlabregex['kota_awalan_J_S'] = dqlabregex['kota'].str.contains('^(j|s)', case = False)

#Tampilkan hasilnya
print(dqlabregex[['kota','kota_awalan_J_S']])