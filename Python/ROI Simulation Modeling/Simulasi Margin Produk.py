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

# Hitung rata-rata margin dari setiap produk dan simpan keseluruhan hasilnya dalam variabel sku_margin
sku_margin = df.groupby('sku_id')['margin_pct'].mean().reset_index()

#Urutkan produk berdasarkan nilai rata-rata margin di sku_margin dari yang tertinggi dan simpan hasil pengurutannya di sku_margin_ranked
sku_margin_ranked = sku_margin.sort_values(by='margin_pct', ascending=False)

#Tampilkan 5 produk dengan rata-rata margin tertinggi
print(sku_margin_ranked.head(5))