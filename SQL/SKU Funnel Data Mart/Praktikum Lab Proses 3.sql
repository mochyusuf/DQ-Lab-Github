/* Data yang akan di-insert ke tabel destinasi */
SELECT 
      STR_TO_DATE(LPAD(`date`, 8, '0'), '%d%m%Y') AS `date`,
      product_id,
      purchase,
      add_to_cart,
      click,
      view,
      'SYSTEM' AS insert_by,
      '2025-08-17 10:00:00' AS insert_date
   FROM tbl_funnels
   WHERE STR_TO_DATE(LPAD(`date`, 8, '0'), '%d%m%Y') = 
   (SELECT MAX(STR_TO_DATE(LPAD(`date`, 8, '0'), '%d%m%Y')) FROM tbl_funnels);