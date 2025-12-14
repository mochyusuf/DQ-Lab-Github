pelanggan <- read.csv("https://storage.googleapis.com/dqlab-dataset/customer_segments.txt",sep="\t")
pelanggan_matrix <- data.matrix(pelanggan[c("Jenis.Kelamin", "Profesi", "Tipe.Residen")])
pelanggan <- data.frame(pelanggan, pelanggan_matrix)
pelanggan$NilaiBelanjaSetahun = pelanggan$NilaiBelanjaSetahun/1000000

#Mengisi data master
Profesi <- unique(pelanggan[c("Profesi", "Profesi.1")])
Jenis.Kelamin <- unique(pelanggan[c("Jenis.Kelamin", "Jenis.Kelamin.1")])
Tipe.Residen <- unique(pelanggan[c("Tipe.Residen", "Tipe.Residen.1")])