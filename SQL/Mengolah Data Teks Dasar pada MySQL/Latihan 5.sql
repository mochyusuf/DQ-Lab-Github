SELECT SUBSTR(isi, LOCATE('|||', isi) + 1, LOCATE('|||', isi, LOCATE('|||', isi) + 3) - LOCATE('|||', isi) - 3) as KotaLahir
FROM dqlabdatateks;