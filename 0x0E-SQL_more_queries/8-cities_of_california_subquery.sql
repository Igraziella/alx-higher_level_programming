-- Lists all cities of California found in hbtn_0d_usa database
-- results are sorted in ascending order by cities id
SELECT id, name FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name = 'Carlifornia')
ORDER BY id  ASC;
