# Gunakan kutip dua untuk setiap string
# Import numpy sebagai aliasnya np
# dan import stats dari scipy
import numpy as np
from scipy import stats

# Baca data survei_tinggi_badan.txt dengan numpy loadtxt
tinggi_badan = np.loadtxt("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt", skiprows=1)
# Tentukan statistik deskriptif tinggi badan 
desc_stat = stats.describe(tinggi_badan)
print("Statistik deskriptif tinggi badan:\n", desc_stat)