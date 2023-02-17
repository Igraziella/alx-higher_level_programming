-- Created the database hbtn_0d_usa and the table cities.
-- cities' id must be unique, a primary key, and not null
-- state id must be a foreign key and not null
CREATE Database IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT NOT NULL AUTO_GENERATED,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id));
