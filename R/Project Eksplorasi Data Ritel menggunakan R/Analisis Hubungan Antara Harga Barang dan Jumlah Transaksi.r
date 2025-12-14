#Analisis hubungan antara Harga Barang dengan Jumlah Transaksi
#Memilih data dengan jenis transaksi Penjualan
data <- data[(data$Jenis.Transaksi) == "Penjualan",]

#Mengubah data harga menjadi Integer
data$Harga <- as.integer(data$Harga)

#Mengubah nilai NA menjadi 0
data$Harga[is.na(data$Harga)] <- 0

#Menghitung jumlah transaksi berdasarkan rentang harga
data_transaksi <- aggregate(
  x=data$No.Transaksi, 
  by = list(Harga = data$Harga), 
  FUN = length)

#Mengurutkan data dari harga termahal
data_transaksi = data_transaksi[order(-data_transaksi$Harga), ]

#Visualisasi data hubungan harga barang dengan jumlah transaksi
#Sebelum menggunakan perintah hist() kamu perlu memecah data transaksi diatas menjadi bentuk data vektor sebagai berikut
data_transaksi_freq = as.vector(rep(data_transaksi$Harga, data_transaksi$x))

#Setelah mendapatkan data diatas, kita dapat mengeluarkan histogram dari tabel diatas dengan menggunakan perintah hist()
hist(data_transaksi_freq,
     main="Hubungan antara harga barang dengan transaksi",
     xlab="Rentang harga barang",
     col="green"
)