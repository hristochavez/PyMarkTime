-- Este script debe de ser ejecutado por algún usuario que tenga permisos
-- en la BBDD para crear a otros usuarios de BBDD.

-- Crea al usuario de la BBDDD.
CREATE USER `usr-dev`@`localhost` IDENTIFIED BY `Hack2024$$`;

-- Crea la BBDD.
CREATE DATABASE pymarktime;

-- Otorga permisos al usuario creado para administrar los objetos de la BBDD 
-- creada.
GRANT 
	ALL PRIVILEGES 
ON 
	pymarktime.* 
TO 
	'usr-dev'@'localhost';

-- Otorga permisos al usuario para administrar procedimientos almacenados de la
-- BBDD.
GRANT 
    ALTER ROUTINE, 
    CREATE ROUTINE, 
    EXECUTE 
ON 
	pymarktime.* 
TO 
	'usr-dev'@'localhost';
