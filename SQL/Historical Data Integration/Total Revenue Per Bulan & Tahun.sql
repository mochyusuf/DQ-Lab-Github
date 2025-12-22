-- Konversi menjadi varchar(8)
WITH transaksi AS (
    SELECT 
        CAST(trx_date AS CHAR) AS trx_date,
        units,
        product_id
    FROM tbl_transaction
    WHERE trx_id IS NOT NULL
), produk AS (
    SELECT DISTINCT
        product_id, 
        CAST(REPLACE(product_price, 'IDR ', '') AS FLOAT) AS product_price
    FROM tbl_product
)
SELECT 
    DATE_FORMAT(
        STR_TO_DATE(
            CASE
                WHEN LENGTH(t.trx_date) = 7 
                    THEN CONCAT(
                        RIGHT(t.trx_date, 4), '-', 
                        SUBSTRING(t.trx_date, 2, 2), '-0', 
                        LEFT(t.trx_date, 1)
                    )
                WHEN LENGTH(t.trx_date) = 8 
                    THEN CONCAT(
                        RIGHT(t.trx_date, 4), '-', 
                        SUBSTRING(t.trx_date, 3, 2), '-', 
                        LEFT(t.trx_date, 2)
                    )
                ELSE NULL
            END, '%Y-%m-%d'
        ), '%M %Y'
    ) AS month_year,
    SUM(t.units * p.product_price) AS revenue
FROM transaksi t
LEFT JOIN produk p 
    ON t.product_id = p.product_id
GROUP BY 1;