#Import Library
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#Membaca dataset
df_merged = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/stock.csv')

#Ukuran figure
plt.figure(figsize = (14, 6))

#Membuat boxplot unit_sold untuk setiap product_category
sns.boxplot(data = df_merged, x = 'product_category', y = 'unit_sold')

#Format visual
plt.title('Boxplot Unit Sold per Product')
plt.xticks(rotation = 45, ha = 'right')
plt.tight_layout()

#Tampilkan plot
plt.show()
