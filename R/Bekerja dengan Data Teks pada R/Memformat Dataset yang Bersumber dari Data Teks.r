#Melakukan import file
data <- read.table(
  file = "https://storage.googleapis.com/dqlab-dataset/datalahir_teks_dqlab.txt",
  header = FALSE, 
  sep = "\n", 
  na.strings=c("NA", "N/A", ""), 
  col.names = 'data_list',
  skip = 1)

#Menampilkan 5 data teratas
head(data,5)

#Memisahkan data menggunakan strsplit
data <- strsplit(data$data_list, split = "|||", fixed = TRUE)

#Merubah data menjadid dataframe
df <- data.frame(matrix(unlist(data), nrow=length(data), byrow=TRUE))

#Memberikan nama pada setiap kolom
colnames(df) <- c('Nama','Tempat_Lahir', 'Tanggal_Lahir', 'Provinsi')

#Tampilkan 5 baris pertama dari df
head(df,5)

#Tambahkan kolom baru yang berisi tempat lahir dan provinsi
df$kota_provinsi <- paste(df$Tempat_Lahir, ",", df$Provinsi)

#Tampilkan 5 data teratas dari df
head(df,5)

#Menghapus karakter yang bukan termasuk alphabet pada kolom Nama
df$Nama <- gsub('\\[^A-Za-z]', '', df$Nama)

#Tampilkan isi dari df
df