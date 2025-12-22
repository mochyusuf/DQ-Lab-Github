/*Data yang akan di-insert ke tabel destinasi */  
   SELECT 
       *,
	   'SYSTEM' AS insert_by,
	   '2025-08-17 10:00:00' AS insert_date
   FROM tbl_lead_time
   WHERE product_id IS NOT NULL
   ORDER BY avg_lead_time