/*Data yang akan di-insert ke table*/
SELECT
   date AS period_date,
   s.product_id,
   stock,
   safety_stock,  
   restock_date,
   quantity AS restock_quantity,
   lt.warehouse_id,
   warehouse_name,
   avg_lead_time,
   'SYSTEM' AS insert_by,
   '2025-08-17 10:00:00' AS insert_date
FROM tbl_dwh_stock_on_hand s
LEFT JOIN tbl_dwh_restock_order ro ON s.date = ro.restock_date AND s.product_id =  ro.product_id
LEFT JOIN tbl_dwh_lead_time lt ON ro.product_id = lt.product_id AND ro.warehouse_id = lt.warehouse_id
