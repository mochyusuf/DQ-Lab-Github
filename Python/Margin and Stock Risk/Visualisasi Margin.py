#Import Library
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
    'stock_available': 'sum'
})

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

# Distribusi kategori margin
plt.figure(figsize = (6, 4))
sns.countplot(data = df, x = 'margin_category', palette = 'Set2')
plt.title('Jumlah Produk per Kategori Margin')
plt.show()