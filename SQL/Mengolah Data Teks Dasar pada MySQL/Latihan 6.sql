SELECT SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 3, 
LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - LOCATE('|||', isi, LOCATE('|||', isi) + 1) - 3) as TanggalLahir
FROM dqlabdatateks;