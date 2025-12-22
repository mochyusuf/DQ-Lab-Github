/*Tampilkan date dan product_id yang muncul lebih dari 1 kali*/
SELECT 
    date,
    product_id,
    COUNT(*) AS jumlah
FROM tbl_funnels
GROUP BY date, product_id
HAVING COUNT(*) > 1;