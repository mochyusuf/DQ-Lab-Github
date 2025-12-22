/* Tampilkan nilai minimum dan maksimum pada kolom trx_date*/
SELECT 
   MIN(trx_date) AS min_date, 
   MAX(trx_date) AS max_date 
FROM tbl_transaction;