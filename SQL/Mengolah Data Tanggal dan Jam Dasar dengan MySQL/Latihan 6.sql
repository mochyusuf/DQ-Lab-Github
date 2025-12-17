SELECT YEAR(tanggal) as tahun, SUM(JUMLAH * HARGA) as total
FROM dqlab_retail
GROUP BY YEAR(tanggal);