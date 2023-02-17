-- Creates a table unique_id on MySQL server
CREATE Table IF NOT EXISTS unique_id (
	id INT DEFAULT 1 NOT NULL,
       	name VARCHAR(256),
	PRIMARY KEY(id));
