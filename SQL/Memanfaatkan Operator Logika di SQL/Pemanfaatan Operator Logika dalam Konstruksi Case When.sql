SELECT DISTINCT
Customer_ID,
Product,
Average_Transaction,
Count_Transaction,
CASE
     WHEN Average_transaction > 2000000 and Count_Transaction > 30 then 'Platinum Member'
     WHEN Average_transaction between 1000000 and 2000000 and Count_Transaction between 20 and 30 then 'Gold Member'
     WHEN Average_transaction < 1000000 and Count_Transaction<20 then 'Silver Member'
         ELSE "Other Membership" end as Membership
FROM summary_transaction