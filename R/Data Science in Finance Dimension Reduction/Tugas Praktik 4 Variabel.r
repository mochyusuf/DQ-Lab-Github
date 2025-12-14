# Panggil library openxlsx untuk membaca file data Excel
# [1]
library(openxlsx)

# Baca data pada sheet "csdata" dalam file "https://storage.googleapis.com/dqlab-dataset/dqlab_pcadata.xlsx
# dan simpan data dengan nama "csdat_raw"
# [2]
csdat_raw <- read.xlsx("https://storage.googleapis.com/dqlab-dataset/dqlab_pcadata.xlsx", sheet = "csdata")

# Tampilkan struktur data
# [3]
str(csdat_raw)

# Tampilkan beberapa baris observasi dengan fungsi head()
# [4]
head(csdat_raw)

# Tampilkan statistika deskriptif untuk semua variabel dalam data.
# [5]
summary(csdat_raw)

# Gambarkan distribusi Income berdasarkan Dependents
library(ggplot2)
ggplot(csdat_raw, aes(as.factor(dependents), income)) +
  geom_boxplot() + xlab("Dependents") + ggtitle("Boxplot Income Berdasarkan Dependents")

# Pisahkan data untuk traning set dan testing set
# untuk tiap-tiap risk rating

# Catat indeks/ nomor baris untuk tiap-tiap risk rating
index1 <- which(csdat_raw$riskrating == 1)
index2 <- which(csdat_raw$riskrating == 2)

# Lakukan pencatatan indeks untuk risk rating berikutnya
# [6]
index3 <- which(csdat_raw$riskrating == 3)
index4 <- which(csdat_raw$riskrating == 4)
index5 <- which(csdat_raw$riskrating == 5)

# 80% data akan digunakan sebagai traning set.
# [7]
ntrain1 <- round(0.8 * length(index1))
ntrain2 <- round(0.8 * length(index2))
ntrain3 <- round(0.8 * length(index3))
ntrain4 <- round(0.8 * length(index4))
ntrain5 <- round(0.8 * length(index5))

# set seed agar sampling ini bisa direproduksi
set.seed(100)

# sampling data masing-masing rating untuk training set
# [8]
train1_index <- sample(index1, ntrain1)
train2_index <- sample(index2, ntrain2)
train3_index <- sample(index3, ntrain3)
train4_index <- sample(index4, ntrain4)
train5_index <- sample(index5, ntrain5)

# menyimpan data ke dalam testing set
# [9]
test1_index <- setdiff(index1, train1_index)
test2_index <- setdiff(index2, train2_index)
test3_index <- setdiff(index3, train3_index)
test4_index <- setdiff(index4, train4_index)
test5_index <- setdiff(index5, train5_index)

# Menggabungkan hasil sampling masing-masing risk rating ke dalam training set
csdattrain <- do.call("rbind", list(csdat_raw[train1_index,],
                                    csdat_raw[train2_index,], csdat_raw[train3_index,],
                                    csdat_raw[train4_index,], csdat_raw[train5_index,]))
cstrain <- subset(csdattrain, select =
                    -c(contractcode,riskrating))

# Menggabungkan hasil sampling masing-masing risk rating ke dalam testing set
csdattest <- do.call("rbind", list(csdat_raw[test1_index,],
                                   csdat_raw[test2_index,], csdat_raw[test3_index,],
                                   csdat_raw[test4_index,], csdat_raw[test5_index,])) # [10]
cstest <- subset(csdattest,
                 select = -c(contractcode,riskrating)) # [11]

# Menghitung korelasi antar variabel
cor(cstrain)

# Lakukan analisa PCA dengan fungsi prcomp() dan
# simpan output ke dalam obyek dengan nama pr.out
# [12]
pr.out <- prcomp(cstrain, scale = TRUE, center = TRUE)

# Tampilkan output PCA dengan memanggil obyek pr.out
# [13]
pr.out

# Tampilkan summary dari output PCA
# [14]
summary(pr.out)

# Gambarkan scree plot dengan menggunakan fungsi screeplot()
# [15]
screeplot(pr.out, type = "line", ylim = c(0,2))

# Tambahkan garis horizontal sebagai panduan untuk menggunakan kriteria Kaiser
abline(h = 1, lty = 3, col = "red")

# Gambarkan biplot dengan menggunakan fungsi biplot()
# [16]
biplot(pr.out, scale = 0) # draw first 2 principal components