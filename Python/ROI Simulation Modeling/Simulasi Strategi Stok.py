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

#Menandai understock: buat kolom understock_flag (TRUE jika spike_flag == 1 dan units_sold > stock_available)
df['understock_flag'] = (df['spike_flag'] == 1) & (df['units_sold'] > df['stock_available'])

#Menghitung lost_units dan lost_revenue saat understock
df['lost_units'] = df.apply(lambda x: max(0, x['units_sold'] - x['stock_available']) if x['understock_flag'] else 0, axis=1)
df['lost_revenue'] = df['lost_units'] * df['unit_price']

#Menandai overstock: buat kolom overstock_flag (TRUE jika stock_available > units_sold)
df['overstock_flag'] = df['stock_available'] > df['units_sold']

#Menghitung excess_units dan holding_cost (holding_rate = 0.10)
df['excess_units'] = df.apply(lambda x: max(0, x['stock_available'] - x['units_sold']) if x['overstock_flag'] else 0, axis=1)
holding_rate = 0.10
df['holding_cost'] = df['excess_units'] * df['unit_price'] * holding_rate * df['restock_lead_days']

#Tampilkan tabel df terbaru
print(df)

#Buat tabel agregasi per SKU bernama sku_stock berisi total lost_units, lost_revenue, excess_units, dan holding_cost
sku_stock = df.groupby('sku_id')[['lost_units','lost_revenue','excess_units','holding_cost']].sum().reset_index()

#Urutkan sku_stock berdasarkan lost_revenue tertinggi. Simpan hasilnya dalam sku_stock_sorted.
sku_stock_sorted = sku_stock.sort_values(by='lost_revenue', ascending=False)

#Tampilkan 5 baris pertama sku_stock_sorted.
print(sku_stock_sorted.head())
