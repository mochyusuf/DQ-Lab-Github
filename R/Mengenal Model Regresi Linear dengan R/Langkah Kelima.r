# Analisis Regresi menggunakan R
data_regresi = data.frame(
bulan = data_delayed_effect$bulan,
tahun = data_delayed_effect$tahun,
kunjungan_dokter = data_delayed_effect$kunjungan_dokter,
penjualan_sereal = data_delayed_effect$penjualan_sereal_4)

# Mengeliminasi data NA
data_regresi = na.omit(data_regresi)

# Model regresi menggunakan R
model = lm(kunjungan_dokter ~ penjualan_sereal, data = data_regresi)

summary(model)