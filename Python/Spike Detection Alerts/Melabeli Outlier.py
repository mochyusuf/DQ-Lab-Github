import pandas as pd

# proses ekstraksi data 
data_trx = pd.read_excel('https://storage.googleapis.com/dqlab-dataset/tbl_transaction.xlsx')

# proses agregasi data 
total_unit_terjual = data_trx.groupby(['trx_date', 'product_id'], as_index = False).agg(total_unit = ('units', 'sum'))

total_unit_terjual_produk019 = total_unit_terjual[total_unit_terjual['product_id'] == 'DQProduk-019']

# definisikan fungsi untuk menghitung outlier
def labelling_outlier(data):
   q1 = data.quantile(0.25)
   q3 = data.quantile(0.75)
   iqr = q3 - q1
   lower_bound = q1 - 1.5*iqr
   upper_bound = q3 + 1.5*iqr
   result = data.apply(lambda x: 'Outlier' if (x < lower_bound) or (x > upper_bound) else 'Inlier')
   return result

# terapkan fungsi
total_unit_terjual_produk019['flag_outlier'] = labelling_outlier(total_unit_terjual_produk019['total_unit'])

# banyak menghitung frekuensi kemunculan flag outlier
print(total_unit_terjual_produk019['flag_outlier'].value_counts())