SELECT YEAR(tanggal) as tahun, MONTH(tanggal) as bulan, 
SUM(jumlah * harga) as total
FROM dqlab_retail
GROUP BY YEAR(tanggal), MONTH(tanggal);