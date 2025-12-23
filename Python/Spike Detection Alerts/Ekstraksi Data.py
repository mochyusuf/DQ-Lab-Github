# import library yang digunakan 
import pandas as pd

# proses ekstraksi data 
data_trx = pd.read_excel('https://storage.googleapis.com/dqlab-dataset/tbl_transaction.xlsx')

# tampilkan sampel data
print(data_trx.head())

# tampilkan informasi umum pada data tersebut
print(data_trx.info())