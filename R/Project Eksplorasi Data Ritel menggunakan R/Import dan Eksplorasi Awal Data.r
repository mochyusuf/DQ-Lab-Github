#Load data dan simpan ke dalam variable bernama ‘data’
data <- read.csv("https://storage.googleapis.com/dqlab-dataset/transaksi_stok_dan_penjualan.tsv", header = TRUE, sep = "\t")

#Tampilkan 5 data teratas 
head(data, 5)

#Tampilkan 5 data terbawah 
tail(data, 5)

#Tampilkan informasi mengenai struktur dari data
str(data)