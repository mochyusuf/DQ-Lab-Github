SELECT CONCAT_WS(' - ',
SUBSTR(isi, LOCATE('|||', isi) + 3, LOCATE('|||', isi, LOCATE('|||', isi) + 1) - LOCATE('|||', isi) - 1),
RIGHT(isi, LENGTH(isi) - LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 1) + 1) - 1 + 1)) AS TempatLahir
FROM dqlabdatateks;