#Import Library
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

#Load data
df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/stock.csv')

#Hitung margin terlebih dahulu
df['margin'] = round(((df['price'] - df['cost']) / df['price']) * 100,2)

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

# Visualisasi distribusi margin
plt.figure(figsize = (8, 4))
sns.histplot(df['margin'], bins = 30, kde = True)
plt.title('Distribusi Profit Margin (%)')
plt.xlabel('Margin (%)')
plt.show()