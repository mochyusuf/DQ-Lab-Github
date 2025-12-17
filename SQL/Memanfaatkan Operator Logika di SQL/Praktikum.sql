SELECT DISTINCT
	Customer_ID, Product,
    Average_transaction,
    Average_transaction >= 1000000 is_eligible
FROM summary_transaction;