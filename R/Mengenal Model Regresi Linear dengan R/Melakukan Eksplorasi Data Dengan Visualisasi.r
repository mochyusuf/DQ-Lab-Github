#Melakukan explorasi data kunjungan dokter dengan penjualan permen
plot(data_gabungan$tingkat.kunjungan.ke.dokter.gigi, data_gabungan$penjualan.permen,
	pch = 19,
    xlab = "Kunjungan dokter",
    ylab = "Penjualan Permen",
    main = "Kunjungan dokter dengan penjualan permen",     
    col = "blue")

#Melakukan explorasi data kunjungan dokter dengan penjualan sereal
plot(data_gabungan$tingkat.kunjungan.ke.dokter.gigi, data_gabungan$penjualan.sereal,
	pch = 19,
    xlab = "Kunjungan dokter",
    ylab = "Penjualan Sereal",
    main = "Kunjungan dokter dengan penjualan sereal",     
    col = "blue")

#Melakukan explorasi data kunjungan dokter dengan penjualan buah pisang
plot(data_gabungan$tingkat.kunjungan.ke.dokter.gigi, data_gabungan$penjualan.buah.pisang,
	pch = 19,
    xlab = "Kunjungan dokter",
    ylab = "Penjualan Buah Pisang",
    main = "Kunjungan dokter dengan penjualan buah pisang",     
    col = "blue")