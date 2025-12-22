/* Konversi menjadi varchar(8) */
WITH transaksi AS ( 
   SELECT 
      trx_date,
      CAST(trx_date AS CHAR(8)) AS trx_date_str
   FROM tbl_transaction
)
SELECT 
   CASE 
      WHEN LENGTH(trx_date_str) = 7 
         THEN STR_TO_DATE(
            CONCAT(
               RIGHT(trx_date_str,4), '-',
               SUBSTRING(trx_date_str,2,2), '-0',
               LEFT(trx_date_str,1)
            ), '%Y-%m-%d'
         )
      WHEN LENGTH(trx_date_str) = 8 
         THEN STR_TO_DATE(
            CONCAT(
               RIGHT(trx_date_str,4), '-',
               SUBSTRING(trx_date_str,3,2), '-',
               LEFT(trx_date_str,2)
            ), '%Y-%m-%d'
         )
      ELSE NULL
   END AS trx_date
FROM transaksi
LIMIT 5;