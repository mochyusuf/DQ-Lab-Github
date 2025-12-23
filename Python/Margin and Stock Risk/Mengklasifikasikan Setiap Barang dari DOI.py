#Import Library
import pandas as pd

#Load data
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/stock.csv')

#Konversi kolom tanggal
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')

#Filter bulan Oktober
df = df[df['date'].dt.month == 10]

#Grup berdasarkan nama produk
df = df.groupby('product_name', as_index=False).agg({
    'unit_sold': 'sum',
    'stock_available': 'sum'
})

#Hindari pembagian nol
df['unit_sold'] = df['unit_sold'].replace(0, pd.NA)

#Hitung DOI
df['doi'] = round(df['stock_available'] / (df['unit_sold'] / 30), 2)

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

print(df)