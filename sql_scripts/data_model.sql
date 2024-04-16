-- Create table employees.
CREATE TABLE employees(
	id INT AUTO_INCREMENT PRIMARY KEY,
	dni VARCHAR(8) NOT NULL,
	first_name VARCHAR(30) NOT NULL,
	pass CHAR(64) NOT NULL,
	CONSTRAINT uniq_dni UNIQUE(dni)
);

-- Insert users.
INSERT INTO 
	employees(dni, first_name, pass)
VALUES 
	('74576066', 'hristo', SHA2('1234', 256)),
	('75328598', 'rosmery', SHA2('1234', 256));