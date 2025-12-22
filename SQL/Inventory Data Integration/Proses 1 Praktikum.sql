/*Data yang akan di-insert ke tabel destinasi*/
SELECT 
          STR_TO_DATE(`date`, '%d/%m/%Y')  AS `date`,
          product_id,
          stock,
          safety_stock,
         'SYSTEM' AS insert_by,
         '2025-08-17 10:00:00' AS insert_date
   FROM tbl_stock_on_hand
   WHERE (product_id IS NOT NULL) AND (STR_TO_DATE(`date`, '%d/%m/%Y') = (
      SELECT MAX(STR_TO_DATE(`date`, '%d/%m/%Y')) FROM tbl_stock_on_hand
    ))
   ORDER BY product_id, `date`