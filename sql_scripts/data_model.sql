-- Creación de tabla de empleados.
CREATE TABLE employees(
	id INT AUTO_INCREMENT PRIMARY KEY,
	dni VARCHAR(8) NOT NULL,
	first_name VARCHAR(30) NOT NULL,
	pass CHAR(64) NOT NULL,
	CONSTRAINT uniq_dni UNIQUE(dni)
);

-- Insertar usuarios.
INSERT INTO 
	employees(dni, first_name, pass)
VALUES 
	('74576066', 'hristo', SHA2('1234', 256)),
	('75328598', 'rosmery', SHA2('1234', 256));

-- Creación de tabla de marcaciones.
CREATE TABLE markings(
	id INT AUTO_INCREMENT PRIMARY KEY,
	dni VARCHAR(8) NOT NULL,
	mark_time DATETIME NOT NULL,
	CONSTRAINT fk_dni_mark FOREIGN KEY (dni)
	REFERENCES employees(dni)
);

-- Insertar marcaciones.
CALL mark('74576066');