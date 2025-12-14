#Perbandingan barang masuk dan keluar perbulan
aggregate(
  x=data$Jumlah, 
  by = list(Bulan = data$Bulan_Tahun, Jenis_Transaksi = data$Jenis.Transaksi), 
  FUN = sum)

#Visualisasikan data dengan chart yang sesuai
#Buat tabel transaksi menggunakan fungsi aggregate
data_transaksi = aggregate(
  x=data$Jumlah, 
  by = list(Bulan = data$Bulan_Tahun, Jenis_Transaksi = data$Jenis.Transaksi), 
  FUN = sum)

#Keluarkan data transaksi penjualan dan stok masuk
data_penjualan <- data_transaksi[(data_transaksi$Jenis_Transaksi) == "Penjualan",]
data_stok_masuk <- data_transaksi[(data_transaksi$Jenis_Transaksi) == "Stok Masuk",]

#Gabungkan kedua data diatas menggunakan fungsi merge dengan left join
data_gabungan = merge(data_stok_masuk,data_penjualan,by='Bulan', all.x=TRUE)
data_gabungan = data.frame(Bulan = data_gabungan$Bulan,
                           Stok_Masuk = data_gabungan$x.x,
                           Penjualan = data_gabungan$x.y)

#Periksa apakah terdapat NA data. Jika terdapat NA data, kamu dapat menggantinya dengan 0
data_gabungan$Penjualan[is.na(data_gabungan$Penjualan)] <- 0

#Ubah format data gabungan dengan melakukan perintah transpose. Lalu ubah nama kolom menggunakan bulan
data_gabung = t(as.matrix(data_gabungan[-1]))
colnames(data_gabung) = data_gabungan$Bulan

#Keluarkan bar plot dengan multiple kategori untuk membandingkan stok masuk dengan penjualan. Lalu keluarkan legend dari barplot tersebut.
barplot(data_gabung,
        main='Perbandingan Penjualan dengan Stok Masuk',
        ylab='Jumlah Barang', 
        xlab='Bulan',
        beside = TRUE, 
        col=c("red","blue"))
legend('topright',fill=c("red","blue"),legend=c('Stok Masuk','Penjualan'))