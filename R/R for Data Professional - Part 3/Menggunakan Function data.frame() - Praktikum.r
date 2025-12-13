#Buatlah vector sesuai dengan instruksi yang sudah diberikan
nama <- c("Kroma", "Andra", "Aksara", "Antara", "Senja")
pekerjaan <- c("Manager", "Senior Data Scientist", "Data Analyst", "Data Engineer", "Senior Data Analyst")
periode_kerja <- c(5, 2, 1, 1, 3)

#Gabungkan ketiga vector menjadi sebuah Dataframe menggunakan data.frame()
df <- data.frame(nama,pekerjaan,periode_kerja)
df

#cek apakah variable df merupakan Dataframe
is.data.frame(df)