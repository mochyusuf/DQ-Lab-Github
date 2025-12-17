SELECT LEFT(
SUBSTR(isi, LOCATE('|||', isi, LOCATE('|||', isi) + 2) + 2, LOCATE('|||', isi, LOCATE('|||', isi, LOCATE('|||', isi) + 2) + 2) - LOCATE('|||', isi, LOCATE('|||', isi) + 2) - 2), 3) AS DD
FROM dqlabdatateks;