SELECT DISTINCT
Customer_ID,
Product,
Average_transaction,
Count_Transaction,
CASE
	WHEN Average_transaction < 1000000 then '4-5x Email dalam seminggu'
    WHEN Average_transaction > 1000000 then '1-2x Email dalam seminggu'
END AS frekuensi_email
FROM summary_transaction