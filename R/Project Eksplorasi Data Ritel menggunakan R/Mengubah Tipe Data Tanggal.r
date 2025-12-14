#Ubah tipe data variabel Tanggal menjadi date
data$Tanggal <- as.Date(data$Tanggal, "%d-%m-%Y")

#Cek apakah tipe data dari variabel Tanggal sudah menjadi date
str(data$Tanggal)

#Tambahkan kolom baru untuk menyimpan data bulan dan tahun
data$Bulan_Tahun <- format(data$Tanggal, "%m-%Y")

#Tampilkan 5 data teratas
head(data, 5)