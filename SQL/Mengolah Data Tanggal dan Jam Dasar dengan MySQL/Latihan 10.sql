SELECT YEAR(tanggal) AS tahun, kode_produk, nama_produk,
SUM(jumlah) AS totaljumlah, harga, SUM(JUMLAH*HARGA) AS total
FROM dqlab_retail
GROUP BY YEAR(tanggal),kode_produk, nama_produk, harga;