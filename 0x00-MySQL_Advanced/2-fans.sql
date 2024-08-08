-- Script that ranks country origins of brands, ordered by the
-- number of fans
SELECT origin, SUm(fans) AS nb_fans
	from metal_bands
	GROUP BY origin
	ORDER BY nb_fans DESC;
