#Konstruksi Dataframe
nama <- c("Kroma", "Andra", "Aksara", "Antara", "Senja")
pekerjaan <- c("Manager", "Senior Data Scientist", "Data Analyst", "Data Engineer", "Senior Data Analyst")
periode_kerja <- c(5,2,1,1,3)
df <- data.frame(nama,pekerjaan,periode_kerja)

#Tampilkan seluruh element pada kolom 'nama' dengan menggunakan $
df$nama

#Tampilkan seluruh element pada kolom 'pekerjaan' dengan menggunakan $
df$pekerjaan

#Tampilkan seluruh element pada kolom 'periode_kerja' dengan menggunakan $
df$periode_kerja