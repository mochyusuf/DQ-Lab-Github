#Import library yang dibutuhkan
import pandas as pd

#Baca file dqlabregex.tsv
dqlabregex = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/dqlabregex.tsv", sep = '\t')

#Ubah karakter pada kolom jumlah_member sesuai ketentuan
mapchange = {'O':'0','I':'1','S':'5'}
dqlabregex['jumlah_member_clean'] = dqlabregex['jumlah_member']

for ubah, pengubah in mapchange.items():
	dqlabregex['jumlah_member_clean'] = dqlabregex['jumlah_member_clean'].str.replace(ubah,pengubah, case = False)

#Tampilkan hasilnya
print(dqlabregex[['jumlah_member','jumlah_member_clean']])