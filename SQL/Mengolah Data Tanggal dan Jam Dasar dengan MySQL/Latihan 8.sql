SELECT kode_produk, nama_produk, SUM(JUMLAH*HARGA) as total
FROM dqlab_retail
GROUP BY kode_produk,nama_produk;