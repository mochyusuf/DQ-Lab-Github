# Membaca library
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Membaca dataset
df_merged = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/stock.csv')

# Ambil daftar unik product_name dan bagi dua
product_names = sorted(df_merged['product_name'].unique())
midpoint = len(product_names) // 2
top_half = product_names[:midpoint]
bottom_half = product_names[midpoint:]

# Filter data untuk masing-masing grup
df_top = df_merged[df_merged['product_name'].isin(top_half)]
df_bottom = df_merged[df_merged['product_name'].isin(bottom_half)]

# Membuat dua subplot vertikal
fig, (ax1, ax2) = plt.subplots(2, 1, figsize = (20, 15), sharey = True)

# Boxplot untuk setengah pertama
sns.boxplot(data = df_top, x = 'product_name', y = 'unit_sold', ax = ax1)
ax1.set_title('Boxplot Unit Sold (Top Half)')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation = 35, ha = 'right')

# Boxplot untuk setengah kedua
sns.boxplot(data = df_bottom, x = 'product_name', y = 'unit_sold', ax = ax2)
ax2.set_title('Boxplot Unit Sold (Bottom Half)')
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=35, ha = 'right')

# Rapi
plt.tight_layout()
plt.show()