#Impor library pandas sebagai pd
import pandas as pd

#Gunakan pandas untuk membaca dataset roi.csv dan simpan dalam variabel df
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/komdigi/tbl_roi.csv')

#Hitung revenue dengan mengalikan kolom unit_price dengan kolom units_sold dan simpan hasilnya dalam kolom revenue
df['revenue'] = df['unit_price'] * df['units_sold']

#Hitung modal dengan mengalikan kolom unit_cost dengan kolom units_sold dan simpan hasilnya dalam kolom cost
df['cost'] = df['unit_cost']  * df['units_sold']

#Hitung margin percentage berdasarkan rumus yang sudah dijelaskan sebelumnya dan simpan dalam kolom margin_pct
df['margin_pct'] = (df['revenue'] - df['cost']) / df['revenue'] * 100

#Menentukan nilai kerugian akibat refund untuk masing-masing record SKU dan simpan dalam kolom refund_loss
df['refund_loss'] = df['units_refunded'] * df['unit_price']

#Menentukan pendapatan yang sudah dikurangi dengan refund_loss dan simpan dalam kolom adjusted_revenue
df['adjusted_revenue'] = df['revenue'] - df['refund_loss']

#Tampilkan tabel df terbaru
print(df)

#Buatkan tabel yang mengandung jumlah penjualan unit dan jumlah pegembalian unit untuk masing-masing produk dan namakan tabel tersebut sku_refund
sku_refund = df.groupby('sku_id')[['units_sold','units_refunded']].sum().reset_index()

#Hitung refund rate sebagai hasil pembagian jumlah pengembalian unit dengan jumlah penjualan unit kemudian dikalikan 100 (satuan persen). Simpan hasil dalam kolom refund_rate
sku_refund['refund_rate'] = sku_refund['units_refunded'] / sku_refund['units_sold'] * 100

#Urutkan tabel sku_refund berdasarkan kolom refund_rate dari nilai yang paling besar. Simpan hasil pengurutannya dalam tabel sku_refund_sorted
sku_refund_sorted = sku_refund.sort_values(by='refund_rate', ascending=False)

#Tampilkan 5 baris pertama tabel sku_refund_sorted
print(sku_refund_sorted.head(5))