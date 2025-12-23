#membaca library
import pandas as pd

#membaca dataset
df_merged = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/funnel.csv')

#Hitung jumlah pelanggan yang menonton iklan sampai membelinya
conversion_by_category = df_merged.groupby('product_category')[['view','purchase']].sum().reset_index()

#Hitung Conversion Rate setiap kategori
conversion_by_category['conversion_rate'] = round((conversion_by_category['purchase']/conversion_by_category['view']) * 100, 2)

#Urutkan dari yang tertinggi nilai conversion rate
conversion_by_category = conversion_by_category.sort_values(by = 'conversion_rate', ascending = False)

#Tampilkan hasil
print("\nConversion Rate per Product Category:")
print(conversion_by_category)