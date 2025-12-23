#Membaca library
import pandas as pd

#Load data
df_merged = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/funnel.csv')

#Hitung jumlah pelanggan yang menonton iklan sampai membelinya
df_merged = df_merged.groupby('product_category')[['view', 'click', 'add_to_cart', 'purchase']].sum().reset_index()

#Hitung absolute drop-off antar tahapan
df_merged['drop_view_click'] = df_merged['view'] - df_merged['click']
df_merged['drop_click_cart'] = df_merged['click'] - df_merged['add_to_cart']
df_merged['drop_cart_purchase'] = df_merged['add_to_cart'] - df_merged['purchase']

#Total drop-off
df_merged['total_dropoff'] = df_merged['drop_view_click'] + df_merged['drop_click_cart'] + df_merged['drop_cart_purchase']

#Tampilkan 10 produk dengan drop-off terbesar
top_dropoff = df_merged[['product_category','total_dropoff']].sort_values(by = 'total_dropoff', ascending=False).head()

print("\n10 Kategori Produk dengan Drop-off Terbesar:")
print(top_dropoff)