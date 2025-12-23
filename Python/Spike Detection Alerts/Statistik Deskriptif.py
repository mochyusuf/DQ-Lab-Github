# import library yang digunakan 
import pandas as pd

# proses ekstraksi data 
data_trx = pd.read_excel('https://storage.googleapis.com/dqlab-dataset/tbl_transaction.xlsx')

# proses agregasi data (gunakan dict agar kompatibel semua versi)
total_unit_terjual = data_trx.groupby(['trx_date', 'product_id'], as_index=False).agg({
    'units': 'sum'
})

# rename kolom supaya sesuai dengan requirement
total_unit_terjual.rename(columns={'units': 'total_unit'}, inplace=True)

# proses filter data 
total_unit_terjual_produk019 = total_unit_terjual[total_unit_terjual['product_id'] == 'DQProduk-019']

# hitung statistik deskriptif
statistics_produk019 = pd.DataFrame({
  'mean' : [total_unit_terjual_produk019['total_unit'].mean()],
  'median' : [total_unit_terjual_produk019['total_unit'].median()],
  'modus' : [total_unit_terjual_produk019['total_unit'].mode()[0] if not total_unit_terjual_produk019['total_unit'].mode().empty else None],
  'min' : [total_unit_terjual_produk019['total_unit'].min()],
  'max' : [total_unit_terjual_produk019['total_unit'].max()],
  'q1' : [total_unit_terjual_produk019['total_unit'].quantile(0.25)],
  'q3' : [total_unit_terjual_produk019['total_unit'].quantile(0.75)],
  'iqr' : [total_unit_terjual_produk019['total_unit'].quantile(0.75) - total_unit_terjual_produk019['total_unit'].quantile(0.25)],
  'stdev' : [total_unit_terjual_produk019['total_unit'].std()],
  'skewness' : [total_unit_terjual_produk019['total_unit'].skew()]
}) 

# Tampilkan hasilnya
print(statistics_produk019)