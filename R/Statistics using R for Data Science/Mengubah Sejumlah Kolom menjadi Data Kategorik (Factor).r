# Mengubah data menjadi factor untuk membedakan data kualitatif dengan menggunakan functon as.factor

data_intro$Jenis.Kelamin <- as.factor(data_intro$Jenis.Kelamin)
data_intro$Produk <- as.factor(data_intro$Produk)
data_intro$Tingkat.Kepuasan <- as.factor(data_intro$Tingkat.Kepuasan)

# Melihat apakah sudah berhasil dalam mengubah variabel tersebut dengan menggunakan function str
str(data_intro$Jenis.Kelamin)
str(data_intro$Produk)
str(data_intro$Tingkat.Kepuasan)