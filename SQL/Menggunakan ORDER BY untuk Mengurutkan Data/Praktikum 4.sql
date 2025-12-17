SELECT
	EXTRACT(YEAR_MONTH from (from_unixtime(Last_Transaction/1000))) month_transaction,
    Customer_ID,
    Product,
    sum(Count_Transaction) total_pembelian_produk
FROM
	data_retail
GROUP BY
	1,2,3
ORDER BY
	1 DESC