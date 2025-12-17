SELECT a.Customer_ID, a.Transaksi_Sepatu, b.Transaksi_Jaket
FROM (select customer_id, sum(count_transaction) transaksi_sepatu
      from data_retail
      where product = 'Sepatu'
      group by 1) A
JOIN (select Customer_ID, sum(Count_Transaction) transaksi_jaket
      from data_retail
      where product = 'Jaket'
      group by 1) B on a.Customer_ID = b.Customer_ID
ORDER BY 2 DESC,3 DESC