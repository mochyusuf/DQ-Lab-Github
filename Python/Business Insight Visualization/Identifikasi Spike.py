# Import library
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Membaca dataset dari file csv
df_transaction = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/tbl_transaction.csv')
df_product = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/tbl_product.csv')

# Menggabungkan dua dataset
df_merged = pd.merge(df_transaction, df_product, on = 'product_id', how = 'left')

# Merapikan format tanggal dan units
df_merged['trx_date'] = pd.to_datetime(df_merged['trx_date'].astype(str), format = '%d%m%Y', errors = 'coerce')
df_merged['units'] = df_merged['units'].fillna(0).astype(int)

# Menghapus nilai kosong dan duplikat
df_merged = df_merged.dropna().drop_duplicates()

# Membuat kolom bulan (periode)
df_merged['trx_month'] = df_merged['trx_date'].dt.to_period('M').dt.to_timestamp()

# Agregasi penjualan per produk per bulan
df_sales_summary = df_merged.groupby(['trx_month', 'product_id', 'product_name'])['units'].sum().reset_index()

# Mengambil 5 produk dengan total units terbanyak
top_products = df_sales_summary.groupby ('product_name')[ 'units'].sum().nlargest(5).index

# Filter hanya untuk 5 produk tersebut
df_top_sales = df_sales_summary[df_sales_summary['product_name'].isin(top_products)].copy()

# Plotting dengan fitur tambahan
plt.figure(figsize=(14, 6))

# Produk target yang akan disorot
target_product = 'Sticky Notes DQLab'

# Warna: produk target tetap cerah, lainnya redup
colors = {
    name: 'dodgerblue' if name == target_product else 'lightgray' for name in df_top_sales['product_name'].unique()
}

# Gambar lineplot tiap produk
for product_name in df_top_sales['product_name'].unique():
    data = df_top_sales[df_top_sales['product_name'] == product_name]
    plt.plot(data['trx_month'], data['units'], label = product_name,
             marker='o', color=colors[product_name])

# Tambahkan lingkaran penanda spike untuk Sticky Notes DQLab di bulan ke-10
data_sticky = df_top_sales[df_top_sales['product_name'] == target_product]
data_sticky = data_sticky.sort_values('trx_month').reset_index(drop = True)

# Asumsikan spike pada bulan ke-10 (indeks ke-5)
if len(data_sticky) >= 10:
    spike_month = data_sticky.loc[5, 'trx_month']
    spike_units = data_sticky.loc[5, 'units']
    plt.scatter(spike_month, spike_units, s = 150, facecolors = 'none',
                edgecolors = 'red', linewidths = 2)
    plt.text(spike_month, spike_units + 500, 'Spike terindikasi', color='red')

# Penataan plot
plt.title('Top 5 Produk Berdasarkan Penjualan per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Total Units Terjual')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend(title='Produk', bbox_to_anchor = (1.05, 1), loc = 'upper left')
plt.tight_layout()
plt.show()