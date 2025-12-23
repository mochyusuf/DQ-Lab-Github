#membaca library
import pandas as pd

#membaca dataset dari file csv
df_transaction = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/tbl_transaction.csv')
df_product = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/tbl_product.csv')

#menggabungkan dua dataset
df_merged = pd.merge(df_transaction, df_product, on = 'product_id', how = 'left')

#mengurutkan dataset yang baru sesuai ketentuan
df_merged = df_merged[['trx_id', 'trx_date', 'product_id', 'product_name', 'product_category', 'product_cost', 'product_price', 'units']]

#merubah format trx_date menjadi tanggal
df_merged['trx_date'] = pd.to_datetime(df_merged['trx_date'].astype(str), format = '%d%m%Y', errors = 'coerce')

#merubah format units menjadi integer
df_merged['units'] = df_merged['units'].fillna(0).astype(int)

#menghapus nilai yang kosong
df_merged = df_merged.dropna()

#menghapus duplikasi
df_merged = df_merged.drop_duplicates()

#menampilkan dataset
print(df_merged.head())