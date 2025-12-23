#Import Library
import pandas as pd

#Load data
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/stock.csv')

#Konversi kolom tanggal
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')

#Filter bulan Oktober
df = df[df['date'].dt.month == 10]

#Hitung margin terlebih dahulu
df['margin'] = round(((df['price'] - df['cost']) / df['price']) * 100, 2)

#Kelompokkan berdasarkan product_name dan hitung rata-rata margin
df = df.groupby('product_name', as_index = False).agg({
    'margin': 'mean',
    'price': 'mean',
    'cost': 'mean',
    'unit_sold': 'sum',
    'stock_available': 'sum'
})

#Hindari pembagian nol
df['unit_sold'] = df['unit_sold'].replace(0, pd.NA)

#Hitung DOI
df['doi'] = round(df['stock_available'] / (df['unit_sold'] / 30),2)

#Urutkan berdasarkan margin terbesar
df = df.sort_values(by = 'margin', ascending = False)

#Buat kategori margin
def margin_category(margin):
    if margin >= 40:
        return 'High'
    elif margin >= 20:
        return 'Medium'
    else:
        return 'Low'

df['margin_category'] = df['margin'].apply(margin_category)

#Klasifikasi DOI
def classify_doi(doi):
    if pd.isna(doi):
        return 'Tidak Terjual'
    elif doi <= 30:
        return 'Cepat Laku'
    elif doi <= 90:
        return 'Normal'
    else:
        return 'Lambat Laku'

df['doi_category'] = df['doi'].apply(classify_doi)

# Tentukan threshold berdasarkan kuartil
margin_q = df['margin'].quantile([0.25, 0.5, 0.75])
doi_q = df['doi'].quantile([0.25, 0.5, 0.75])

# Buat fungsi klasifikasi kuadran
def classify_sku(row):
    if row['margin'] >= margin_q[0.75] and row['doi'] <= doi_q[0.25]:
        return 'Produk Bintang'
    elif row['margin'] >= margin_q[0.75] and row['doi'] > doi_q[0.75]:
        return 'Bintang Tapi Tidak Stabil'
    elif row['margin'] < margin_q[0.25] and row['doi'] <= doi_q[0.25]:
        return 'Penggerak Volume'
    elif row['margin'] < margin_q[0.25] and row['doi'] > doi_q[0.75]:
        return 'Perlu Evaluasi / Stop'
    else:
        return 'Lainnya'

# Terapkan klasifikasi
df['sku_category'] = df.apply(classify_sku, axis=1)

# Tampilkan hasil
print(df)