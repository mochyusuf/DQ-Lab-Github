# Import math
import math
# Jumlah anggota populasi
N = 8963
# Proporsi
p = 0.25
# z-score
z = 1.96
# Margin of error
e = 0.05
# Perhitungan ukuran sampel, n
n_aksen = z**2 * p * (1 - p) / e**2
n = n_aksen / (1 + (n_aksen / N))
# Cetak jumlah sampel
print("Jumlah sampel:", math.ceil(n))