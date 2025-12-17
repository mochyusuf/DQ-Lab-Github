SELECT tanggal, SUM(jumlah * harga) as total
FROM dqlab_retail
GROUP BY tanggal;