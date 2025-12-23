# import library yang digunakan 
import pandas as pd

# proses ekstraksi data 
data_trx = pd.read_excel('https://storage.googleapis.com/dqlab-dataset/tbl_transaction.xlsx')

# proses agregasi data 
total_unit_terjual = data_trx.groupby(['trx_date', 'product_id'], as_index = False).agg(total_unit = ('units', 'sum'))

# tampilkan hasilnya
print(total_unit_terjual.head())