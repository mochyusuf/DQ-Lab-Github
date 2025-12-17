SELECT
	Customer_ID, Product, average_transaction_amount,
    product = 'Jaket' AND average_transaction_amount >= 1000000 loyal_buyer_jaket
FROM data_retail
WHERE product = 'Jaket'