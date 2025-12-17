SELECT 
    SUBSTR(
        SUBSTR(
            isi, 
            LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, 
            LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - 
            LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3
        ), 
        4,  
        LENGTH(SUBSTR(
            isi, 
            LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, 
            LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - 
            LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3
        )) - 8  
    ) AS Bulan  
FROM 
    dqlabdatateks;