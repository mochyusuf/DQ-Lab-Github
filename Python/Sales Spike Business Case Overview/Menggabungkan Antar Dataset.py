#membaca library
import pandas as pd

#membaca dataset dari file csv
df_transaction = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/tbl_transaction.csv')
df_product = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/tbl_product.csv')

#menggabungkan dua dataset
df_merged = pd.merge(df_transaction, df_product, on = 'product_id', how = 'left')

#mengurutkan dataset yang baru sesuai ketentuan
df_merged = df_merged[['trx_id','trx_date','product_id','product_name','product_category','product_cost','product_price','units']]

#menampilkan dataset
print(df_merged.head())