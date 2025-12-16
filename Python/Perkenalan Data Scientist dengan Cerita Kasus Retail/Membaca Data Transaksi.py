#Mengimpor library pandas & numpy
import pandas as pd
import numpy as np

#Membaca file
dataset_transaksi = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/transaksi_dqlab_retail.tsv', sep='\t')

#Menampilkan isi data
print(dataset_transaksi)