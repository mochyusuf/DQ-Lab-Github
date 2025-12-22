/* Tampilkan product_id yang muncul lebih dari 1 kali */
SELECT 
    product_id,
    COUNT(*) AS frekuensi
FROM tbl_product
GROUP BY product_id
HAVING COUNT(*) > 1;