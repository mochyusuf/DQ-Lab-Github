# Import numpy sebagai aliasnya np
import numpy as np

# Baca dataset 
tinggi_badan = np.loadtxt("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt", skiprows=1)

# Cetak ukuran dataset dan isinya
print("Ukuran data tinggi_badan:", tinggi_badan.shape)
print("Data tinggi_badan (cm):\n", tinggi_badan)