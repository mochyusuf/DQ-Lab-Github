SELECT
	Customer_ID, Count_Transaction,
    (
    SELECT AVG(Count_Transaction)
    		FROM data_retail
            WHERE product = 'Sepatu'
    ) Avg_Transaction
FROM data_retail
WHERE product = 'Sepatu'