/*Kalkulasi total kolom perhitungan*/
WITH funnels AS ( 
    SELECT 
         CAST(date AS CHAR) AS trx_date,
         product_id,
         SUM(purchase) AS total_purchase,
         SUM(add_to_cart) AS total_add_to_cart,
         SUM(click) AS total_click,
         SUM(view) AS total_view
   FROM tbl_funnels
   GROUP BY trx_date, product_id
),
produk AS (
   SELECT DISTINCT 
      product_id, CAST(REPLACE(product_price, 'IDR ', '') AS FLOAT) AS product_price, product_name, product_category 
   FROM tbl_product
)
SELECT
      CAST( 
         CASE
            WHEN LENGTH(f.trx_date) = 7 
               THEN CONCAT(RIGHT(f.trx_date, 4), '-', SUBSTRING(f.trx_date, 2, 2), '-0', LEFT(f.trx_date, 1))
            WHEN LENGTH(f.trx_date) = 8
               THEN CONCAT(RIGHT(f.trx_date, 4), '-', SUBSTRING(f.trx_date, 3, 2), '-', LEFT(f.trx_date, 2))
            ELSE NULL
         END
      AS DATE) AS trx_date,
      f.product_id,
      p.product_name,
      p.product_category,
      f.total_purchase,
      f.total_add_to_cart,
      f.total_click,
      f.total_view 
   FROM funnels f
   LEFT JOIN produk p ON f.product_id = p.product_id;
