-- Script that creates a database and a table

-- Query to create database

SELECT id, name FROM cities WHERE state_id = (
	SELECT id FROM states  WHERE name = "California"
);
