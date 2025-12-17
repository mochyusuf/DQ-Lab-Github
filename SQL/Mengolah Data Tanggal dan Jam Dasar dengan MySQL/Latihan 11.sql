SELECT YEAR(tanggal) AS tahun, MONTH(tanggal) AS bulan, kode_produk, nama_produk,
SUM(jumlah) AS totaljumlah, harga, SUM(jumlah*harga) AS total
FROM dqlab_retail
GROUP BY YEAR(tanggal), MONTH(tanggal),kode_produk, nama_produk, harga;