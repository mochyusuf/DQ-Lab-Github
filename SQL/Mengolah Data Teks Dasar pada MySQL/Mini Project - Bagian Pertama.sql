SELECT 
    LEFT(isi, LOCATE('|||', isi) - 1) AS Nama,
    SUBSTR(isi, LOCATE('|||', isi) + 3, LOCATE('|||', isi, LOCATE('|||', isi) + 1) - LOCATE('|||', isi) - 3) AS KotaLahir,
    SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, 
           LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3) AS TanggalLahir,
    RIGHT(isi, LENGTH(isi) - LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - 3 +1) AS Propinsi
FROM dqlabdatateks;