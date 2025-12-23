#Import Library
import pandas as pd
from scipy.stats import zscore
import numpy as np

#Membaca dataset dari file CSV
df_merged = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/stock.csv')

#Menghitung z-score untuk kolom unit_sold
df_merged['zscore_unit_sold'] = zscore(df_merged['unit_sold'])

#Filter data yang merupakan outlier (z-score < -3 atau > 3)
outliers_z = df_merged[(df_merged['zscore_unit_sold'] < -3) | (df_merged['zscore_unit_sold'] > 3)].copy()

#Menambahkan kolom apakah outlier termasuk lower atau upper
outliers_z['outlier_type'] = np.where(
    outliers_z['zscore_unit_sold'] < -3, 'lower', 'upper'
)

#Menampilkan semua outlier
print(outliers_z.head())