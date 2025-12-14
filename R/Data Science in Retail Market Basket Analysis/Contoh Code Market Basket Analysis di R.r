#Menggunakan library arules
library(arules)

#Membaca transaksi dari file data_transaksi.txt
transaksi <- read.transactions(file="https://storage.googleapis.com/dqlab-dataset/data_transaksi.txt", format="single", sep="\t", cols=c(1,2), skip=1)

#Menampilkan data transaksi dengan print dan inspect 
inspect(transaksi)

#Menghasilkan model Market Basket Analysis
mba <- apriori(transaksi,parameter = list(supp = 0.1, confidence = 0.5))

#Menampilkan paket produk
inspect(subset(mba, lift>1))