-- Lists all cities of California found in hbtn_0d_usa database
SELECT cities FROM hbtn_0d_usa.states
WHERE name = Carlifornia
ORDER BY cities.id  ASC;
