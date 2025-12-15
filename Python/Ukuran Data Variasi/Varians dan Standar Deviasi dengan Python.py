# Import numpy
import numpy as np
# Baca dataset
tinggi_badan = np.loadtxt("https://storage.googleapis.com/dqlab-dataset/survei_tinggi_badan.txt", skiprows=1)

def py_rata_rata(data):
	return sum(data) / len(data)

def py_varians(data, k=1):
	rerata, var = py_rata_rata(data), 0
	for d in data:
		var += (d - rerata) ** 2
	return var / (len(data) - k)

def py_standar_deviasi(data, k=1):
	return py_varians(data, k=k) ** 0.5

print("Menggunakan user-defined function pada array tinggi_badan")
print("unbiased varians :", py_varians(tinggi_badan))
print("biased varians :", py_varians(tinggi_badan, k=0))
print("unbiased standar deviasi:", py_standar_deviasi(tinggi_badan))
print("biased standar deviasi :", py_standar_deviasi(tinggi_badan, k=0))

print("\nMenggunakan method .var() dan .std() pada array tinggi_badan")
print("unbiased varians :", tinggi_badan.var(ddof=1))
print("biased varians :", tinggi_badan.var())
print("unbiased standar deviasi:", tinggi_badan.std(ddof=1))
print("biased standar deviasi :", tinggi_badan.std())