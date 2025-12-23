#Import Library
import pandas as pd

#Load data
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/stock.csv')

#Konversi kolom tanggal
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')

#Filter bulan Oktober
df = df[df['date'].dt.month == 10]

#Kelompokkan berdasarkan product_name
df = df.groupby('product_name', as_index = False).agg({
    'unit_sold': 'sum',
    'stock_available': 'sum'})

#Menentukan Threshold dengan kuartil
stock_Q3 = df['stock_available'].quantile(0.75)
sold_Q1 = df['unit_sold'].quantile(0.25)
sold_Q3 = df['unit_sold'].quantile(0.75)

#Mencetak nilai kuartil
print('Kuartil ke-3 dari stok tersedia adalah:', stock_Q3)
print('Kuartil ke-1 dari stok terjual adalah:', sold_Q1)
print('Kuartil ke-3 dari stok terjual adalah:', sold_Q3)
print('Barang dikatakan Overstocked jika stock_available >', stock_Q3, 'dan unit_sold <', sold_Q1)
print('Barang dikatakan Lowerstocked jika stock_available >', stock_Q3, 'dan unit_sold >', sold_Q3)