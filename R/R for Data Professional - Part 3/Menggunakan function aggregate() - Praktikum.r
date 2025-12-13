#Konstruksi Dataframe
nama <- c("Andra","Andra","Senja","Senja","Aksara","Aksara","Kroma","Kroma")
hari <- c("Senin","Selasa","Senin","Selasa","Senin","Selasa","Senin","Selasa")
jam_kerja <- c(8,9,8,8,9,9,8,10)
data <- data.frame(nama,hari,jam_kerja)
data

#Jumlah jam kerja tiap individu
aggregate(data$jam_kerja, list(data$nama), sum)

#Rata-rata jam kerja berdasarkan hari
aggregate(data$jam_kerja, list(data$hari), mean)