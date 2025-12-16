#Import library yang dibutuhkan
import pandas as pd

#Baca file dqlabregex.tsv
dqlabregex = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dqlabregex.tsv", sep = '\t')

#Sintaks merapikan format tanggal pada kolom tanggal_catat
dqlabregex['tanggal_catat'] = dqlabregex['tanggal_catat'].str.replace('([0-9]{2})-([0-9]{2})-([0-9]{4})','\\2/\\1/\\3')

#Tampilkan hasilnya
print(dqlabregex[['tanggal_catat']])