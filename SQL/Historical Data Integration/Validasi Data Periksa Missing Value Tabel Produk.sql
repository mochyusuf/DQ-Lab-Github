/* Tampilkan semua data jika product_id atau product_price kosong */
SELECT * FROM tbl_product
WHERE product_id is NULL OR product_price is NULL