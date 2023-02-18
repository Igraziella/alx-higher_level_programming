-- Creates the database hbtn_0d_usa and the table states
-- states id must be unique, auto generated, primary key and not null
CREATE Database IF NOT EXISTS hbtn_0d_usa;
CREATE Table IF NOT EXISTS hbtn_0d_usa.states (
	id INT UNIQUE NOT NULL AUTO_GENERATE,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id));
