/* Data yang akan di-insert ke tabel destinasi  */
SELECT      
    trx_id,
	product_id,
    STR_TO_DATE(
        CONCAT(
            SUBSTRING(LPAD(trx_date, 8, '0'), 1, 2), '-', 
            SUBSTRING(LPAD(trx_date, 8, '0'), 3, 2), '-', 
            SUBSTRING(LPAD(trx_date, 8, '0'), 5, 4)
        ),
        '%d-%m-%Y'
    ) AS trx_date,
    COALESCE(units, 0) AS units,
    'SYSTEM' AS insert_by,
    '2025-08-17 10:00:00' AS insert_date
FROM tbl_transaction
WHERE trx_id IS NOT NULL
  AND STR_TO_DATE(
        CONCAT(
            SUBSTRING(LPAD(trx_date, 8, '0'), 1, 2), '-', 
            SUBSTRING(LPAD(trx_date, 8, '0'), 3, 2), '-', 
            SUBSTRING(LPAD(trx_date, 8, '0'), 5, 4)
        ),
        '%d-%m-%Y'
    ) = (
        SELECT MAX(
            STR_TO_DATE(
                CONCAT(
                    SUBSTRING(LPAD(trx_date, 8, '0'), 1, 2), '-', 
                    SUBSTRING(LPAD(trx_date, 8, '0'), 3, 2), '-', 
                    SUBSTRING(LPAD(trx_date, 8, '0'), 5, 4)
                ),
                '%d-%m-%Y'
            )
        )
        FROM tbl_transaction
        WHERE trx_id IS NOT NULL
    );