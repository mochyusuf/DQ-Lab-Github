#Konstruksi Dataframe
nama <- c("Kroma", "Andra", "Aksara", "Antara", "Senja")
pekerjaan <- c("Manager", "Senior Data Scientist", "Data Analyst", "Data Engineer", "Senior Data Analyst")
periode_kerja <- c(5,2,1,1,3)
df <- data.frame(nama,pekerjaan,periode_kerja)

#Tampilkan 3 baris pertama dari kolom 'pekerjaan'
df[1:3,'pekerjaan']

#Tampilkan 2 baris pertama dari kolom 'periode_kerja'
df[1:2,'periode_kerja']