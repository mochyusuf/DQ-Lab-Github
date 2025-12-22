WITH transaction AS (
   SELECT
      product_id,
      trx_date,
      SUM(units) AS total_unit
   FROM tbl_dwh_transaction
   WHERE trx_date = (SELECT MAX(trx_date) FROM tbl_dwh_transaction)
   GROUP BY product_id, trx_date
),
product AS (
    SELECT DISTINCT
      product_id,
      product_cost,
      product_price
   FROM tbl_dwh_product
),
funnels AS (
    SELECT DISTINCT
      `date`,
      product_id,
      SUM(purchase)    AS total_purchase,
      SUM(add_to_cart) AS total_add_to_cart,
      SUM(click)       AS total_click,
      SUM(view)        AS total_view
   FROM tbl_dwh_funnels
   WHERE `date` = (SELECT MAX(`date`) FROM tbl_dwh_funnels)
   GROUP BY `date`, product_id
)
SELECT 
      t.product_id,
      t.trx_date,
      t.total_unit,
      p.product_cost AS cost_each,
      p.product_price AS price_each,
      t.total_unit * p.product_price AS total_price,
      t.total_unit * (p.product_price - p.product_cost) AS total_profit,
      f.total_purchase,
      f.total_add_to_cart,
      f.total_click,
      f.total_view,
      'SYSTEM' AS insert_by,
      '2025-08-17 10:00:00' AS insert_date
FROM funnels AS f 
LEFT JOIN transaction AS t 
      ON t.product_id = f.product_id 
     AND t.trx_date = f.date
INNER JOIN product AS p 
      ON t.product_id = p.product_id;