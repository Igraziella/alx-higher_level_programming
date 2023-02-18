-- Lists all cities contained in the hbtn_0d_usa database
SELECT *
FROM hbtn_0d_usa
INNER JOIN cities.id, cities.name, states.name
ORDER BY id ASC;
