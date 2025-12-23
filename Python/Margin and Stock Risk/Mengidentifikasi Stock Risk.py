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

#Mengkategorikan Stock Risk
df['stock_risk'] = df.apply(
    lambda row: 'Overstocked' if row['stock_available'] > stock_Q3 and row['unit_sold'] < sold_Q1
    else 'Lowerstocked' if row['stock_available'] > stock_Q3 and row['unit_sold'] > sold_Q3
    else 'Normal',
    axis=1
)

print(df)