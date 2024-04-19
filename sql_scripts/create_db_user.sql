-- Create the user for the database.
CREATE USER `usr-dev`@`localhost` IDENTIFIED BY `Hack2024$$`;

-- Create the database.
CREATE DATABASE pymarktime;

-- Give permissions to the user created in the database.
GRANT 
	ALL PRIVILEGES 
ON 
	pymarktime.* 
TO 
	'usr-dev'@'localhost';

-- Give permissions to create and run store procedures.
GRANT 
    ALTER ROUTINE, 
    CREATE ROUTINE, 
    EXECUTE 
ON 
	pymarktime.* 
TO 
	'usr-dev'@'localhost';