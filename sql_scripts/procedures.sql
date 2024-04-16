USE `marcaciones`;
DROP PROCEDURE IF_EXISTS `login_employee`;
DELIMITER $
CREATE PROCEDURE login_employee(
    IN dni VARCHAR(8),
    IN pass CHAR(64)
)
BEGIN
    SELECT 
        x.dni,
        x.first_name
    FROM 
        employees AS x
    WHERE 
        x.dni = dni AND 
        x.pass = pass;
END $
DELIMITER ;