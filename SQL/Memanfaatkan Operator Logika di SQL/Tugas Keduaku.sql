SELECT DISTINCT
	Customer_ID
FROM data_retail_undian
WHERE NOT (Unik_produk >= 3 AND Rata_rata_transaksi >= 1500000)