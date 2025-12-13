#variable sisa_cuti
sisa_cuti <- c(13,10,6,12,7)
 
#variable nama_karyawan
nama_karyawan <- c("Senja","Aksara","Antara","Kroma","Andra")
 
#memberi nama pada sisa_cuti
names(sisa_cuti) <- nama_karyawan
 
#karyawan yang memiliki sisa cuti lebih dari 10
sisa_cuti[sisa_cuti > 10]
 
#karyawan dengan sisa cuti terkecil
min(sisa_cuti)
 
#rata-rata sisa cuti karyawan
mean(sisa_cuti)