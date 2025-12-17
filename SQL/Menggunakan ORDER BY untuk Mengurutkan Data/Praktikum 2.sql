SELECT DISTINCT
    Customer_ID, 
    sum(Count_Transaction) total_transaksi
FROM data_retail
GROUP BY 1
ORDER BY 2 ASC