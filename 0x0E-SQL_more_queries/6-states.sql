-- Script that creates an user and a database in MySQL server
-- Query to create the user 'user_0d_1' and the database 'hbtn_0d_2' in MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);