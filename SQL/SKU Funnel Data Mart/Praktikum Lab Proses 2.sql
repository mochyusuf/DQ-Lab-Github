/* Data yang akan di-insert ke tabel destinasi  */ 
SELECT
    product_id,
    product_name,
    product_category,
    CAST(REPLACE(REPLACE(product_cost, 'IDR', ''), ',', '') AS DECIMAL(15,0)) AS product_cost,
    CAST(REPLACE(REPLACE(product_price, 'IDR', ''), ',', '') AS DECIMAL(15,0)) AS product_price,
    'SYSTEM' AS insert_by,
    '2025-08-17 10:00:00' AS insert_date
FROM tbl_product
WHERE product_id IS NOT NULL
GROUP BY product_id, product_name, product_category, product_cost, product_price;
