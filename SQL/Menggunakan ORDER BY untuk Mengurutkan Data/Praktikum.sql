SELECT
	Customer_ID,
    Product,
    sum(Count_Transaction) total_pembelian_produk
FROM
	data_retail
GROUP BY
	Customer_ID, Product
ORDER BY 1,3 DESC;