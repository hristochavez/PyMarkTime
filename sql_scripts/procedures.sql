-- Procedimiento almacenado para inicio de sesión de empleados.
USE marcaciones;
DROP PROCEDURE IF_EXISTS login_employee;
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
        t1.pass = pass;
END $
DELIMITER ;

-- Procedimiento almacenado para que empleados hagan sus marcaciones.
USE pymarktime;
DROP PROCEDURE IF_EXISTS create_mark;
DELIMITER $
CREATE PROCEDURE create_marktime(
    IN dni CHAR(8)
)
BEGIN
	INSERT INTO markings(dni, mark_time)
	VALUES (dni, NOW());
END $
DELIMITER ;
