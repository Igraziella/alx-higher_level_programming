-- Lists all cities contained in the hbtn_0d_usa database
SELECT *
FROM hbtn_0d_usa
FULL JOIN cities.id, cities.name, states.name
ORDER BY cities.id ASC;
