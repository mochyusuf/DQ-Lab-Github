data_gabungan = merge(kunjungan_dokter, penjualan_permen, by.x=c("Bulan","Tahun"), by.y=c("Bulan","Tahun"), sort=FALSE)
data_gabungan