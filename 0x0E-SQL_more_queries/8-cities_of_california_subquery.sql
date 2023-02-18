-- Lists all cities of California found in hbtn_0d_usa database
-- results are sorted in ascending order by cities id
SELECT id, name FROM cities
WHERE state_id IN (
	SELECT id FROM states
	WHERE name = 'California')
ORDER BY id;
