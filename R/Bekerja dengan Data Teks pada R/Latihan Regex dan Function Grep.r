#Mencari Nama yang mengandung angka
name_with_num <- grep('\\d+', df$Nama)
name_with_num

#Menampilkan data Nama yang mengandung angka
df[name_with_num,]

#Menghapus karakter yang bukan termasuk alphabet
df$Nama <- gsub('\\[^A-Za-z]', '', df$Nama)