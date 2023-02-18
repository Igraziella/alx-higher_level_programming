-- Lists all cities contained in the hbtn_0d_usa database
-- list is sorted in order of ascending cities.id
SELECT c.id, c.name, s.name
FROM cities AS c
INNER JOIN states AS s
ON c.state_id = s.id
ORDER BY c.id ASC;
