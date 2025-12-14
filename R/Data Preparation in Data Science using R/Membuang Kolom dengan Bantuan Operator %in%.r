#Membaca dataset csv
penduduk.dki.csv <-read.csv("https://storage.googleapis.com/dqlab-dataset/dkikepadatankelurahan2013.csv", sep=",")
#Membuang kolom X, X.1, X.2 s/d X.11
penduduk.dki.csv <- penduduk.dki.csv[,!names(penduduk.dki.csv) %in%
                                       c("X","X.1","X.2","X.3","X.4","X.5","X.6",
                                         "X.7","X.8","X.9","X.10", "X.11")]
names(penduduk.dki.csv)