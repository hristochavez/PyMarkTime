from models.employees import get_employee
from templates.employee_menu import employee_menu
import templates.login
import hashlib


# Retorna un SHA256 hash generado de una cadena.
def hash_password(employee_pass):
    return hashlib.sha256(employee_pass.encode()).hexdigest()


# Envia los datos para un inicio de sesión de un empleado.
def login_employee(dni, password):
    # Comunicación con el modelo.
    result = get_employee(dni, hash_password(password))

    # Si retorna más de un empleado llama al menú de empleados.
    if len(result):
        dni = result[0][0]
        first_name = result[0][1]
        permissions = []
        for row in result:
            permissions.append(row[2])

        employee = {
            'dni': dni,
            'first_name': first_name,
            'permissions': permissions
        }

        employee_menu(employee)
    else:
        # Si no retorna ningun resultado vuelve a mostrar el menú de inicio de
        # sesión.
        templates.login.login_screen(fail=True)
