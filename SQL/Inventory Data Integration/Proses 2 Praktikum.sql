   SELECT 
       restock_id,
       STR_TO_DATE(restock_date, '%d/%m/%Y') AS restock_date,
       product_id,
       quantity,
       ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY STR_TO_DATE(restock_date, '%d/%m/%Y') ASC) AS sequence_no,
       warehouse_id,
       'SYSTEM' AS insert_by,
       '2025-08-17 10:00:00' AS insert_date
   FROM tbl_restock_order
   WHERE (product_id IS NOT NULL) 