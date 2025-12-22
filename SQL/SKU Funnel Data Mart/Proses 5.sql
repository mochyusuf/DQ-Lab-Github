/* Data yang akan di-insert ke d_date */
SELECT
    '2025-08-17' - INTERVAL 1 DAY AS `date`,
    DAYNAME('2025-08-17' - INTERVAL 1 DAY) AS day_name,
    MONTHNAME('2025-08-17' - INTERVAL 1 DAY) AS month_name,
    YEAR('2025-08-17' - INTERVAL 1 DAY) AS year,
    'SYSTEM' AS insert_by,
    '2025-08-17 10:00:00' AS insert_date