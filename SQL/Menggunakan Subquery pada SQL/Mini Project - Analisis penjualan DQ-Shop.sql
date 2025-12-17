SELECT 
A.product, 
A.total_buyer, 
D.loyal_customer
FROM (
   SELECT product, COUNT(DISTINCT customer_id) total_buyer
   FROM data_retail
   GROUP BY 1) A
JOIN (
   SELECT B.Product, COUNT(DISTINCT Customer_ID) loyal_customer
   FROM data_retail B
   JOIN (
    SELECT Product, AVG(Count_Transaction) AS Count_Transaction
    FROM data_retail 
    GROUP BY 1
   ) C ON C.Product = B.Product AND B.Count_Transaction > C.Count_Transaction
   GROUP BY 1
   ) D ON A.Product = D.Product