# Ketik perintah berikut ini untuk membaca help tentang matriks
?matrix

# Buatlah matriks 3 x 3 dan simpan dengan nama matriks A.
A <- matrix(c(1,1,0,0,-2,1,0,0,3), nrow = 3, ncol = 3, byrow = TRUE)

# Tuliskan perintah untuk menampilkan matriks A
A

# Tuliskan perintah R untuk menghitung nilai eigen dan vektor eigen
# dan simpanlah hasilnya dalam variable ev
#[3]
ev <- eigen(A)

# Tuliskan perintah untuk melihat struktur obyek eigen
#[4]
str(ev)

# Tuliskan perintah untuk melihat hasil output
#[5]
ev

# Tuliskan perintah untuk mengakses nilai eigen
#[6]
ev$values

# Tuliskan perintah untuk mengakses vektor eigen
#[7]
ev$vectors