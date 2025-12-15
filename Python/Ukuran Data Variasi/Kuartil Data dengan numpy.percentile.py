# Import numpy
import numpy as np
# Baca dataset 
tinggi_badan = np.loadtxt("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt", skiprows=1)

# Perhitungan Q1, Q2, dan Q3 satu persatu
print("Perhitungan Q1, Q2, dan Q3 satu persatu")
Q1 = np.percentile(tinggi_badan, 25)
Q2 = np.percentile(tinggi_badan, 50)
Q3 = np.percentile(tinggi_badan, 75)
print("Kuartil 1 (Q1):", Q1)
print("Kuartil 2 (Q2):", Q2)
print("Kuartil 3 (Q3):", Q3)

# Perhitungan Q1, Q2, dan Q3 sekaligus
print("\nPerhitungan Q1, Q2, dan Q3 sekaligus")
Q123 = np.percentile(tinggi_badan, [25, 50, 75])
print("[Q1, Q2, Q3]:", Q123)