# Import pandas sebagai aliasnya yaitu pd
import pandas as pd

# Baca dataset
tinggi_badan = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt")
# Cetak type(tinggi_badan) dan data frame tinggi_badan sendiri
print("type(tinggi_badan):", type(tinggi_badan))
print(tinggi_badan)

# Hitung statistik deskriptif tinggi_badan
statistik_deskriptif = tinggi_badan.describe()
# Cetak statistik deskriptif tinggi_badan
print("\nStatistik deskriptif:\n", statistik_deskriptif)

# Tentukan IQR
Q1 = statistik_deskriptif["tinggi badan (cm)"]["25%"]
Q3 = statistik_deskriptif["tinggi badan (cm)"]["75%"]
IQR = Q3 - Q1
#Cetak IQR
print("\nIQR:", IQR)

# Persentil ke-5 dan ke-95
percentile = tinggi_badan.quantile(q=[0.05, 0.95])
print("\nPersentil ke-5 dan ke-95:\n", percentile)