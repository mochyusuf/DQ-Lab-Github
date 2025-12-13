#Tambahkan kolom baru yang berisi tempat lahir dan provinsi
df$kota_provinsi <- paste(df$Tempat_Lahir, ",", df$Provinsi)

#Tampilkan 5 data teratas dari df
head(df, 5)