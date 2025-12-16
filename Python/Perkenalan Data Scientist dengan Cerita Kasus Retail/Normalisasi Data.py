#Kode sebelumnya
import pandas as pd
import numpy as np

dataset_transaksi = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/transaksi_dqlab_retail.tsv', sep='\t')
dataset_transaksi['Flag'] = 1

basket = dataset_transaksi.groupby(['Kode Transaksi','Nama Barang'])['Flag'].sum().unstack().reset_index().fillna(0).set_index('Kode Transaksi')

#Membuat function untuk menormalisasi data
def encode_units(x):
	if x <= 0:
		return 0
	if x > 0:
		return 1

#Menerapkan fungsi encode_units pada dataset	
basket_encode = basket.applymap(encode_units)

#Menampilkan basket_encode
print(basket_encode)