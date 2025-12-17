SELECT DISTINCT
Customer_ID
FROM summary_transaction
WHERE Average_transaction < 1000000 and product =  'Sepatu';