SELECT 
    Customer_ID,
    Product,
    Average_Transaction_Amount,
    product = 'Jaket' XOR average_transaction_amount > 1000000 logika_xor
FROM data_retail;