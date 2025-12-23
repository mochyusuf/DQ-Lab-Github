# import library yang digunakan
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# proses ekstraksi data 
data_trx = pd.read_excel('https://storage.googleapis.com/dqlab-dataset/tbl_transaction.xlsx')

# proses agregasi data 
total_unit_terjual = data_trx.groupby(['trx_date', 'product_id'], as_index=False).agg(
    total_unit=('units', 'sum')
)

# filter untuk produk DQProduk-019
total_unit_terjual_produk019 = total_unit_terjual[total_unit_terjual['product_id'] == 'DQProduk-019']

# buat histogram
sns.histplot(total_unit_terjual_produk019['total_unit'])

# hapus tepian
sns.despine()

# tampilkan grafiknya
plt.show()