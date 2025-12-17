SELECT 
	EXTRACT(YEAR_MONTH from (from_unixtime(Last_Transaction/1000))) year_month_transaction,
   	sum(Count_Transaction) total_pembelian_produk
FROM
	data_retail
WHERE 
	Product = 'Sepatu' AND
    EXTRACT(YEAR from (from_unixtime(Last_Transaction/1000))) in (2018, 2019)
GROUP BY
	1
ORDER BY 
	2 ASC
LIMIT 
	3