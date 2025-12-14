#Ubah tipe data variabel Harga menjadi numerik
data$Harga <- as.numeric(data$Harga)

#Ubah data NA menjadi 0
data$Harga[is.na(data$Harga)] <- 0

#Cek apakah tipe data dari variabel Harga sudah menjadi tipe numerik
str(data$Harga)

#Tampilkan 5 data teratas
head(data, 5)