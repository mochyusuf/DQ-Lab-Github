#Lalu ambillah data dengan jenis transaksi adalah Penjualan
data_penjualan = data[data$Jenis.Transaksi=="Penjualan",]

#Lakukan fungsi aggregasi data untuk mendapatkan penjualan perbulan
penjualan_perbulan = aggregate(x=data_penjualan$Jumlah, 
                     by = list(Bulan_Tahun = data_penjualan$Bulan_Tahun),
                     FUN = sum)

#Keluarkan bar plot dari penjualan perbulan
barplot(penjualan_perbulan$x,
        names.arg =penjualan_perbulan$Bulan_Tahun,
        xlab="Month",
        ylab="Penjualan",
        col="blue",
        main="Penjualan perbulan",
        border="red")