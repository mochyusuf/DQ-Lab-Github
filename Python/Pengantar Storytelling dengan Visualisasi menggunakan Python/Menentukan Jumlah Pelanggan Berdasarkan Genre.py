#Kode sebelumnya
import pandas as pd

dataset_shopping = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/shopping_data.csv', delimiter=',')

##Menghitung jumlah pelanggan berdasarkan Genre
#Mencari pembeli dengan jenis kelamin pria
Male_dataset = dataset_shopping[(dataset_shopping["Genre"]=="Male")].reset_index()
jumlah_pria = Male_dataset["Genre"].count()
print("Jumlah Pelanggan Pria =",jumlah_pria)

#Mencari data yang sama pada pembeli dengan jenis kelamin wanita
Female_dataset = dataset_shopping[(dataset_shopping["Genre"]=="Female")].reset_index()
jumlah_wanita = Female_dataset["Genre"].count()
print("Jumlah Pelanggan Wanita =",jumlah_wanita)