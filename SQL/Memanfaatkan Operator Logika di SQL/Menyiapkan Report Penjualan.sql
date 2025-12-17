SELECT DISTINCT
Product Produk,
avg(Average_transaction) 'Jumlah transaksi (Rupiah)',
sum(Count_Transaction) 'Barang terjual'
FROM summary_transaction
GROUP BY Product