#Konstruksi Dataframe
nama <- c("Kroma", "Andra", "Aksara", "Antara", "Senja")
pekerjaan <- c("Manager", "Senior Data Scientist", "Data Analyst", "Data Engineer", "Senior Data Analyst")
periode_kerja <- c(5,2,1,1,3)
df <- data.frame(nama,pekerjaan,periode_kerja)

#Tampilkan kelas atau tipe data dari tiap kolom pada df dengan menggunakan lapply()
l_apply <- lapply(df, class)

#tampilkan isi dari variable l_apply
l_apply

#tampilkan class dari variable l_apply
class(l_apply)

#Tampilkan kelas atau tipe data dari tiap kolom pada df dengan menggunakan sapply()
s_apply <- sapply(df, class)

#tampilkan isi dari variable s_apply
s_apply

#tampilkan class dari variable s_apply
class(s_apply)