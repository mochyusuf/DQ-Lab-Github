#Import Library
import pandas as pd
import numpy as np

#Membaca dataset
df_merged = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/stock.csv')

#Hitung Q1, Q3, dan IQR
Q1 = df_merged['unit_sold'].quantile(0.25)
Q3 = df_merged['unit_sold'].quantile(0.75)
IQR = Q3 - Q1

#Hitung batas bawah dan atas
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

#Filter outliers
outliers_iqr = df_merged[(df_merged['unit_sold'] < lower_bound) | (df_merged['unit_sold'] > upper_bound)].copy()

#Tambahkan kolom jenis outlier (lower / upper)
outliers_iqr['outlier_type'] = np.where(
    outliers_iqr['unit_sold'] < lower_bound, 'lower', 'upper'
)

#Tampilkan hasil
print(outliers_iqr.head())