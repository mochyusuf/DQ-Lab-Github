# 2, Menggabungkan dua dataset menggunakan R dan eliminasi kolom
merge(kunjungan_dokter, penjualan, by=c("Bulan","Tahun"))
data_gabungan = merge(kunjungan_dokter, penjualan, by.x=c("Bulan","Tahun"), by.y=c("Bulan","Tahun"),sort = FALSE)
data_gabungan