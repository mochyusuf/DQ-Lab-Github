SELECT
	SUM(REGEXP_REPLACE(jumlah_member, '[^0-9]', '')) AS total_member,
	REGEXP_REPLACE(staf_pencatat, 'Sen.?ja', 'Senja') AS staf_pencatat
FROM dqlabregex
GROUP BY 2 ORDER BY 1;