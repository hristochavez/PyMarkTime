-- Usar la BBDD pymarktime.
USE pymarktime;

------------
-- TABLAS --
------------

-- Creación de tabla de empleados.
CREATE TABLE employees(
	dni CHAR(8) NOT NULL,
	first_name VARCHAR(30) NOT NULL,
	pass CHAR(64) NOT NULL,
	is_enabled TINYINT(1) DEFAULT 1 NOT NULL,
	updated_by CHAR(8),
	CONSTRAINT pk_dni PRIMARY KEY (dni),
	CONSTRAINT fk_dni_updated_by FOREIGN KEY (updated_by) REFERENCES employees(dni)
);

-- Creación de tabla de marcaciones.
CREATE TABLE markings(
	id INT NOT NULL AUTO_INCREMENT,
	dni CHAR(8) NOT NULL,
	mark_time DATETIME NOT NULL,
	CONSTRAINT pk_id PRIMARY KEY (id),
	CONSTRAINT fk_dni_marking FOREIGN KEY (dni) REFERENCES employees(dni)
);

-- Creación de tabla permisos.
CREATE TABLE permissions(
	id INT NOT NULL AUTO_INCREMENT,
	description VARCHAR(255),
	CONSTRAINT pk_id PRIMARY KEY (id)
);

-- Creación de tabla que 	relaciona empleados y sus permisos.
CREATE TABLE employee_permission(
	dni CHAR(8) NOT NULL,
	permission INT NOT NULL,
	CONSTRAINT pk_dni_permission PRIMARY KEY (dni, permission),
	CONSTRAINT fk_dni FOREIGN KEY (dni) REFERENCES employees(dni),
	CONSTRAINT fk_permissions FOREIGN KEY (permission) REFERENCES permissions(id)
);

--------------------------------
-- PROCEDIMIENTOS ALMACENADOS --
--------------------------------

-- Retorna al empleado para un inicio de sesíon.
DROP PROCEDURE IF_EXISTS get_employee;
DELIMITER $
CREATE PROCEDURE get_employee(
    IN dni CHAR(8),
    IN pass CHAR(64)
)
BEGIN
    SELECT
		t1.dni,
		t1.first_name,
		t2.permission
	FROM
		employees AS t1
	INNER JOIN
		employee_permission AS t2
	ON
		t1.dni = t2.dni
    WHERE
    	t1.dni = dni AND 
        t1.pass = pass AND
       	t1.is_enabled = 1;
END $
DELIMITER ;

-- Crea la marcación de un empleado.
DROP PROCEDURE IF_EXISTS create_marktime;
DELIMITER $
CREATE PROCEDURE create_marktime(
    IN dni CHAR(8)
)
BEGIN
	INSERT INTO markings(dni, mark_time)
	VALUES (dni, NOW());
END $
DELIMITER ;

-- Crea a un empleado.
DROP PROCEDURE IF_EXISTS create_employee;
DELIMITER $
CREATE PROCEDURE create_employee(
	IN dni CHAR(8),
	IN first_name VARCHAR(30)
)
BEGIN
	-- Por defecto crea la contraseña 1234 al empleado recien creado.
	DECLARE pass CHAR(64);
	SELECT SHA2('1234', 256) INTO pass;

	INSERT INTO employees(dni, first_name, pass)
	VALUES(dni, first_name, pass);
	
	INSERT INTO employee_permission(dni, permission)
	VALUES(dni, 1);
END $
DELIMITER ;

-- Deshabilita a un empleado.
DROP PROCEDURE IF_EXISTS disable_employee;
DELIMITER $
CREATE PROCEDURE disable_employee(
	IN dni CHAR(8),
	IN updated_by CHAR(8)
)
BEGIN
	UPDATE employees AS t1
	SET t1.is_enabled = 0, t1.updated_by = updated_by
	WHERE t1.dni = dni;
END $
DELIMITER ;

-- Retorna la información de un empleado.
DROP PROCEDURE IF_EXISTS employee_information;
DELIMITER $
CREATE PROCEDURE employee_information(
	IN dni CHAR(8)
)
BEGIN
	SELECT
		t1.first_name,
		t1.is_enabled
	FROM
		employees AS t1
	WHERE
		t1.dni = dni;
END $
DELIMITER ;
