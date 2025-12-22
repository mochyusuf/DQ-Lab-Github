/* Tampilkan trx_id yang muncul lebih dari 1 kali */
SELECT *
FROM tbl_transaction
WHERE trx_id IN (
    SELECT trx_id
    FROM tbl_transaction
    GROUP BY trx_id
    HAVING COUNT(*) > 1
);
