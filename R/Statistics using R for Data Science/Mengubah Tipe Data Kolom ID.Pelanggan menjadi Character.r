## mengubah data menjadi karakter karena tidak dilakukan analisis statistik pada variabel ID Pelanggan dan nama
data_intro$ID.Pelanggan<-as.character(data_intro$ID.Pelanggan)
data_intro$Nama<-as.character(data_intro$Nama)
str(data_intro$ID.Pelanggan)
## melihat apakah sudah berhasil dalam mengubah variabel tersebut
str(data_intro$Nama)