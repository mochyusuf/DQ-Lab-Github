library (dplyr)
data_delayed_effect = data.frame(
month = data_gabungan$Bulan,
year = data_gabungan$Tahun,
kunjungan_dokter = data_gabungan$tingkat.kunjungan.ke.dokter.gigi,
penjualan_permen = data_gabungan$penjualan.permen,
penjualan_permen_1 = lag(data_gabungan$penjualan.permen),
penjualan_permen_2 = lag(data_gabungan$penjualan.permen,2),
penjualan_permen_3 = lag(data_gabungan$penjualan.permen,3),
penjualan_permen_4 = lag(data_gabungan$penjualan.permen,4),
penjualan_permen_5 = lag(data_gabungan$penjualan.permen,5),
penjualan_permen_6 = lag(data_gabungan$penjualan.permen,6)
)
data_delayed_effect